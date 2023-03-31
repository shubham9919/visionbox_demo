FROM scratch
ADD x86_64/112981945fed42e8b92700af2ca4332462bb17e987b259bdd2b4557571581839.tar.xz /
ADD x86_64/2f62fb45ad589f7ec555c9f3d306c1b200d58bbbab061ad72b26ad59968022ca.tar.xz /
ADD x86_64/53e8701459942ca5f1bada6c1f0072a75d88616f402983cb4fdd8bb778190ee2.tar.xz /
ADD x86_64/7452329f69994dab79c6d1014cf482c3cdc13c00e6d0986599c5a8414c14fe66.tar.xz /
ADD x86_64/7829ac41fab0373bf7e054ee844a8b5016a7a3ac054c320610febadc7208831b.tar.xz /
ADD x86_64/ab9d9129920555ffefd35aacf0daced3b090b37853d524bcd91c68c4df6b4d0b.tar.xz /

ENV LANG=en_US.UTF-8
ENV TZ=:/etc/localtime
ENV PATH=/var/lang/bin:/usr/local/bin:/usr/bin/:/bin:/opt/bin
ENV LD_LIBRARY_PATH=/var/lang/lib:/lib64:/usr/lib64:/var/runtime:/var/runtime/lib:/var/task:/var/task/lib:/opt/lib
ENV LAMBDA_TASK_ROOT=/var/task
ENV LAMBDA_RUNTIME_DIR=/var/runtime

WORKDIR /var/task

ENTRYPOINT ["/lambda-entrypoint.sh"]

FROM public.ecr.aws/lambda/python:3.8

# Install the function's dependencies using file requirements.txt
# from your project folder.

COPY requirements.txt  .
RUN  pip3 install -r requirements.txt --target "${LAMBDA_TASK_ROOT}"

# Copy function code
COPY . ${LAMBDA_TASK_ROOT}

# Set the CMD to your handler (could also be done as a parameter override outside of the Dockerfile)
CMD [ "application.handler" ]