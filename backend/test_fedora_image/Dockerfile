FROM fedora:latest

LABEL maintainer="grudinov.alex@gmail.com"

SHELL ["/bin/bash", "-c"]

RUN sed -i '/tsflags=nodocs/d' /etc/dnf/dnf.conf && \
	yum update -y && \
	yum upgrade -y && \
	yum install -y man-pages man-db man ncurses vim groff neofetch cowsay htop openssh-server cracklib-dicts && \
	mandb && \
	dnf update && \
	echo 'istl2024' | passwd --stdin root && \
	sed -i 's/#PermitRootLogin prohibit-password/PermitRootLogin yes/' /etc/ssh/sshd_config && \
	ssh-keygen -t rsa -f /etc/ssh/ssh_host_rsa_key -N '' && \
	adduser trainee && \
	echo 'istl2024' | passwd --stdin trainee && \
	usermod -aG wheel trainee

COPY my_banner_message /etc/motd.d

EXPOSE 22

CMD ["/usr/sbin/sshd", "-D"]
