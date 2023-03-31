import io
import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
import boto3
import time
import psycopg2
from datetime import datetime


# Load the MNIST dataset
def handler(event=None, context=None):
    mnist = tf.keras.datasets.mnist
    (train_images, train_labels), (test_images, test_labels) = mnist.load_data()

    # Normalize the images
    train_images = train_images / 255.0
    test_images = test_images / 255.0

    # Define the model architecture
    model = tf.keras.Sequential([
    tf.keras.layers.Flatten(input_shape=(28, 28)),
    tf.keras.layers.Dense(128, activation='relu'),
    tf.keras.layers.Dense(10, activation='softmax')
    ])

    # Compile the model
    model.compile(optimizer='adam',
                loss='sparse_categorical_crossentropy',
                metrics=['accuracy'])

    # Train the model
    history = model.fit(train_images, train_labels, epochs=5, validation_data=(test_images, test_labels))

    # Evaluate the model on test data
    test_loss, test_acc = model.evaluate(test_images, test_labels)
    print('Test accuracy:', test_acc)

    # Predict on test data
    predictions = model.predict(test_images)
    predicted_labels = np.argmax(predictions, axis=1)

    # Visualize some predictions
    fig, ax = plt.subplots()

    plt.figure(figsize=(10,10))
    for i in range(25):
        plt.subplot(5,5,i+1)
        plt.imshow(test_images[i], cmap=plt.cm.binary)
        plt.title(f"Predicted label: {predicted_labels[i]}\nTrue label: {test_labels[i]}")
        plt.xticks([])
        plt.yticks([])
    buf = io.BytesIO()
    plt.savefig(buf, format='png')
    buf.seek(0)

    key=str(f'predicted_image_{int(time.time())}.jpg'),
    s3 = boto3.client('s3')
    s3.put_object(
        Bucket='---- s3 bucket name -----',
        Key=f'predicted_image_{int(time.time())}.jpg',
        Body=buf,
        ContentType='image/png'
    )
    print(f"Image { key } saved to ---- s3 bucket name -----/{key}")

    conn = psycopg2.connect(
        host="----------- RDS HOST ----------",
        database="postgres",
        user="postgres",
        password="------ password -------", 
        port=5432,
        options=f"-c search_path={'test2'}" # slecting schema 'test2'
    )

    cur = conn.cursor()
    # Query data from a table
    table_name = "models"
    column_names = ["timets", "image_name"]

    # Define the values for the new row
    values = [
    (datetime.now(), key)
    ]

    # Construct the INSERT query with dynamic variables and values
    query = f"INSERT INTO {table_name} ({','.join(column_names)}) VALUES %s"

    # Execute the query with the values
    cur.execute(query, values)

    # Commit the changes to the database
    conn.commit()

    cur.close()
    conn.close()
    plt.show()

handler() 