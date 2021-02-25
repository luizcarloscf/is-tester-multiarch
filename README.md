<h1 align="center"> is-tester-multiarch </h1>

</p>
<p align="center">
    <a href="https://github.com/luizcarloscf/is-tester-multiarch/actions" alt="build">
         <img src="https://img.shields.io/github/workflow/status/luizcarloscf/is-tester-multiarch/Docker?style=flat-square" /> </a>
    <a href="https://hub.docker.com/r/luizcarloscf/is-tester-multiarch" alt="pulls">
         <img src="https://img.shields.io/docker/pulls/luizcarloscf/is-tester-multiarch?style=flat-square" /> </a>
    <a href="https://github.com/luizcarloscf/is-tester-multiarch/tags" alt="tags">
         <img src="https://img.shields.io/github/v/tag/luizcarloscf/is-tester-multiarch?style=flat-square" /> </a>
    <a href="https://hub.docker.com/r/luizcarloscf/is-tester-multiarch" alt="image-size">
         <img src="https://img.shields.io/docker/image-size/luizcarloscf/is-tester-multiarch?style=flat-square" /> </a>
    <a href="https://github.com/luizcarloscf/is-tester-multiarch/blob/main/LICENSE" alt="license">
         <img src="https://img.shields.io/github/license/luizcarloscf/is-tester-multiarch" /> </a>
    <a href="https://hub.docker.com/r/luizcarloscf/is-tester-multiarch" alt="arch">
         <img src="https://img.shields.io/static/v1?label=OS/arch&message=linux%2Famd64%20%7C%20linux%2F386%20%7C%20linux%2Farm%2Fv6%20%7C%20linux%2Farm%2Fv7%20%7C%20linux%2Farm64%20%7C%20linux%2Fppc64le%20%7C%20linux%2Fs390x&color=blue&style=flat-square" /> </a>
</p>

Simple service for the *is* architecture capable of running in multi-platforms. It is a simple implementation just to prove that any application can be packaged into several docker images supporting different platforms.

## Multi-platform images

> Docker images can support multiple architectures, which means that a single image may contain variants for different architectures, and sometimes for different operating systems, such as Windows. When running an image with multi-architecture support, docker will automatically select an image variant which matches your OS and architecture. Most of the official images on Docker Hub provide a variety of architectures. For example, the busybox image supports amd64, arm32v5, arm32v6, arm32v7, arm64v8, i386, ppc64le, and s390x. When running this image on an x86_64 / amd64 machine, the x86_64 variant will be pulled and run. [See more](https://docs.docker.com/docker-for-mac/multi-arch/).

Docker has an experimental feature called *Buildx*:

> Docker Buildx is a CLI plugin that extends the docker command with the full support of the features provided by [Moby BuildKit](https://github.com/moby/buildkit) builder toolkit. It provides the same user experience as docker build with many new features like creating scoped builder instances and building against multiple nodes concurrently.

When you invoke a build, you can set the `--platform` flag to specify the target platform for the build output, (for example, linux/amd64, linux/arm64, darwin/amd64).

You can build multi-platform images using three different strategies that are supported by Buildx and Dockerfiles:

* Using the QEMU emulation support in the kernel;
* Building on multiple native nodes using the same builder instance;
* Using a stage in Dockerfile to cross-compile to different architectures;

This project uses Github Actions to setup a workflow responsible to build and publish the docker images. It uses QEMU, for emulation of different platforms. All Github Actions used in this project are developed by Docker.

- [docker/setup-qemu-action](https://github.com/docker/setup-qemu-action);

- [docker/setup-buildx-action](https://github.com/docker/setup-buildx-action);

- [docker/login-action](https://github.com/docker/login-action);

- [docker/build-push-action](https://github.com/docker/build-push-action).


## RPC

The RPC, or Remote Procedure Call, provided here acts as a remote server that binds an specific function to a topic. The python script responsible for the RPC in the table below can be found in [`src/is_tester_multiarch/rpc.py`](https://github.com/luizcarloscf/is-tester-multiarch/blob/master/src/is_tester_multiarch/rpc.py).

| Service | Request | Reply |  Description |
| ------- | ------- | ----- | ------------ |
| :incoming_envelope: **topic:** `Tester.Increment`| :gem: **schema:** [Struct] | :gem: **schema:** [Struct] | RPC server that increments 1. |

- Note: run the `is-tester-multiarch-rpc` in container to use this function.

## Configuration

The behavior of the service can be customized by passing a JSON configuration file as the first argument, e.g: `is-tester-multiarch config.json`. The schema for this file can be found in [`src/conf/options.proto`](https://github.com/luizcarloscf/is-tester-multiarch/blob/master/src/is_tester_multiarch/conf/options.proto).

An example configuration file can be found in [`etc/conf/options.json`](https://github.com/luizcarloscf/is-tester-multiarch/blob/master/etc/conf/options.json).

## Example client

In [`example`](https://github.com/luizcarloscf/is-tester-multiarch/blob/master/example) folder there is a python script showing how to test this application. It also has a [`requirements.txt`](https://github.com/luizcarloscf/is-tester-multiarch/blob/master/example/requirement.txt) file to setup packages that the  client script requires. You can install and execute it,

```bash
# clone this repository
$ git clone https://github.com/luizcarloscf/is-tester-multiarch.git

# enter in source code folder
$ cd is-tester-multiarch

# install requirements for client.py script using pip
$ pip3 install -r example/requirements.txt

# execute test
$ python3 example/client.py

```

In [`example/client.py`](https://github.com/luizcarloscf/is-tester-multiarch/blob/master/example/client.py), remember to specify the right  broker address. **If needed**, open it using a text editor and edit the broker URI.

[Struct]: https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#google.protobuf.Struct