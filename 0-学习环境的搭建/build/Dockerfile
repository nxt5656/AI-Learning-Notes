FROM ubuntu:24.04 AS build_apt
SHELL ["/bin/bash", "-c"]
LABEL maintainer="nxt5656@live.cn"
RUN apt update && apt install -y \
    make \
    git \
    python3 \
    python3-pip \
    wget \
    curl \
    nano \
    vim \
    supervisor \
    easy-rsa \
    openssh-server \
    passwd \
    net-tools

FROM build_apt AS build_miniconda
ENV  PATH="/root/miniconda3/bin:${PATH}"
RUN  mkdir -p /root/miniconda3 && wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh -O /root/miniconda3/miniconda.sh
RUN  bash /root/miniconda3/miniconda.sh -b -u -p /root/miniconda3 && rm -rf /root/miniconda3/miniconda.sh
RUN  conda init  bash && source /root/.bashrc
RUN  conda create --name ai-learning-notes python=3.12

FROM build_miniconda AS build_jupyterlab
RUN conda install -n ai-learning-notes -c conda-forge jupyterlab jupyterlab-language-pack-zh-CN ipykernel && \
    conda run -n ai-learning-notes python -m ipykernel install --user --name=ai-learning-notes --display-name "Python (ai-learning-notes)"

FROM build_jupyterlab AS base
LABEL org.opencontainers.image.source=https://github.com/nxt5656/ai-learning-notes
LABEL org.opencontainers.image.description="ai学习笔记"
LABEL org.opencontainers.image.licenses=MIT
WORKDIR /workspace
ADD --chmod=600 0-学习环境的搭建/build/supervisord.conf /devops/supervisord.conf
ADD --chmod=600 0-学习环境的搭建/build/jupyter_lab_config.py /devops/jupyter_lab_config.py
RUN mkdir /var/run/sshd
RUN ssh-keygen -A
RUN sed -i 's/#PermitRootLogin prohibit-password/PermitRootLogin yes/' /etc/ssh/sshd_config
RUN sed -i 's/#PasswordAuthentication yes/PasswordAuthentication yes/' /etc/ssh/sshd_config
RUN echo "root:UserPas$0w" | chpasswd
ADD . /workspace/notes
ENTRYPOINT ["supervisord","-c","/devops/supervisord.conf"]
