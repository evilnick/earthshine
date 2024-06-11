---
wrapper_template: "templates/docs/markdown.html"
markdown_includes:
  nav: kubernetes/docs/shared/_side-navigation.md
context:
  title: 'Kubernetes-worker charm '
  description: The workload bearing units of a kubernetes cluster
keywords: component, charms, versions, release
tags:
    - reference
sidebar: k8smain-sidebar
permalink: 1.16/charm-kubernetes-worker.html
layout:
    - base
    - ubuntu-com
toc: false
charm_revision: '613'
bundle_release: '1.16'
---

This charm deploys a container runtime and the Kubernetes
worker applications: kubelet, and kube-proxy.

In order for this charm to be useful, it should be deployed with its companion
charm kubernetes-master and linked with an SDN-Plugin and a container runtime
such as containerd.

This charm is part of the [Charmed Kubernetes bundle](https://jaas.ai/charmed-kubernetes/bundle) bundle which can be deployed with a single command::

```bash
juju deploy charmed-kubernetes
```

For more information about Charmed Kubernetes see the [overview documentation](/kubernetes/docs/overview)

## Scale out

To add additional compute capacity to your Kubernetes workers, you may
`juju add-unit kubernetes-worker` to scale the cluster. The new units will
automatically join any related kubernetes-master, and enlist themselves as
ready once the deployment is complete.

## Snap Configuration

The Kubernetes resources used by this charm are snap packages. When not
specified during deployment, these resources come from the public store. By
default, the snapd daemon will refresh all snaps installed from the store
four (4) times per day. A charm configuration option is provided for operators
to control this refresh frequency.


### Examples:

##### refresh kubernetes-worker snaps every tuesday

```bash
juju config kubernetes-worker snapd_refresh="tue"
```

##### refresh snaps at 11pm on the last (5th) friday of the month

```bash
juju config kubernetes-worker snapd_refresh="fri5,23:00"
```
##### delay the refresh as long as possible

```bash
juju config kubernetes-worker snapd_refresh="max"
```

##### use the system default refresh timer

```bash
juju config kubernetes-worker snapd_refresh=""
```


For more information, see the [snap documentation](/kubernetes/docs/snap-refresh).

## Configuration


<!-- CONFIG STARTS -->
<!--AUTOGENERATED CONFIG TEXT - DO NOT EDIT -->


| name | type   | Default      | Description                               |
|------|--------|--------------|-------------------------------------------|
| <a id="table-allow-privileged"> </a> allow-privileged | string | true | This option is now deprecated and has no effect.  |
| <a id="table-channel"> </a> channel | string | 1.17/stable | Snap channel to install Kubernetes worker services from  |
| <a id="table-default-backend-image"> </a> default-backend-image | string | auto | Docker image to use for the default backend. Auto will select an image based on architecture.  |
| <a id="table-ingress"> </a> ingress | boolean | True | Deploy the default http backend and ingress controller to handle ingress requests.  |
| <a id="table-ingress-ssl-chain-completion"> </a> ingress-ssl-chain-completion | boolean | False | [See notes](#ingress-ssl-chain-completion-description)  |
| <a id="table-ingress-ssl-passthrough"> </a> ingress-ssl-passthrough | boolean | False | Enable ssl passthrough on ingress server. This allows passing the ssl connection through to the workloads and not terminating it at the ingress controller.  |
| <a id="table-kubelet-extra-args"> </a> kubelet-extra-args | string |  | [See notes](#kubelet-extra-args-description)  |
| <a id="table-kubelet-extra-config"> </a> kubelet-extra-config | string | {} | [See notes](#kubelet-extra-config-description)  |
| <a id="table-labels"> </a> labels | string |  | Labels can be used to organize and to select subsets of nodes in the cluster. Declare node labels in key=value format, separated by spaces.  |
| <a id="table-nagios_context"> </a> nagios_context | string | juju | [See notes](#nagios_context-description)  |
| <a id="table-nagios_servicegroups"> </a> nagios_servicegroups | string |  | A comma-separated list of nagios servicegroups. If left empty, the nagios_context will be used as the servicegroup  |
| <a id="table-nginx-image"> </a> nginx-image | string | auto | Docker image to use for the nginx ingress controller. Auto will select an image based on architecture.  |
| <a id="table-proxy-extra-args"> </a> proxy-extra-args | string |  | [See notes](#proxy-extra-args-description)  |
| <a id="table-require-manual-upgrade"> </a> require-manual-upgrade | boolean | True | When true, worker services will not be upgraded until the user triggers it manually by running the upgrade action.  |
| <a id="table-snap_proxy"> </a> snap_proxy | string |  | DEPRECATED. Use snap-http-proxy and snap-https-proxy model configuration settings. HTTP/HTTPS web proxy for Snappy to use when accessing the snap store.  |
| <a id="table-snap_proxy_url"> </a> snap_proxy_url | string |  | DEPRECATED. Use snap-store-proxy model configuration setting. The address of a Snap Store Proxy to use for snaps e.g. http://snap-proxy.example.com  |
| <a id="table-snapd_refresh"> </a> snapd_refresh | string | max | [See notes](#snapd_refresh-description)  |
| <a id="table-sysctl"> </a> sysctl | string | [See notes](#sysctl-default) | [See notes](#sysctl-description)  |

---

### ingress-ssl-chain-completion


<a id="ingress-ssl-chain-completion-description"> </a>
**Description:**

Enable chain completion for TLS certificates used by the nginx ingress
controller.  Set this to true if you would like the ingress controller
to attempt auto-retrieval of intermediate certificates.  The default
(false) is recommended for all production kubernetes installations, and
any environment which does not have outbound Internet access.

[Back to table](#table-ingress-ssl-chain-completion)


### kubelet-extra-args


<a id="kubelet-extra-args-description"> </a>
**Description:**

Space separated list of flags and key=value pairs that will be passed as arguments to
kubelet. For example a value like this:

```
  runtime-config=batch/v2alpha1=true profiling=true
```

will result in kubelet being run with the following options:

```
  --runtime-config=batch/v2alpha1=true --profiling=true
```

Note: As of Kubernetes 1.10.x, many of Kubelet's args have been deprecated, and can
be set with kubelet-extra-config instead.

[Back to table](#table-kubelet-extra-args)


### kubelet-extra-config


<a id="kubelet-extra-config-description"> </a>
**Description:**

Extra configuration to be passed to kubelet. Any values specified in this
config will be merged into a KubeletConfiguration file that is passed to
the kubelet service via the --config flag. This can be used to override
values provided by the charm.

Requires Kubernetes 1.10+.

The value for this config must be a YAML mapping that can be safely
merged with a KubeletConfiguration file. For example:

```
  {evictionHard: {memory.available: 200Mi}}
```


For more information about KubeletConfiguration, see upstream docs:
https://kubernetes.io/docs/tasks/administer-cluster/kubelet-config-file/

[Back to table](#table-kubelet-extra-config)


### nagios_context


<a id="nagios_context-description"> </a>
**Description:**

Used by the nrpe subordinate charms.
A string that will be prepended to instance name to set the host name
in nagios. So for instance the hostname would be something like:

```
    juju-myservice-0
```

If you're running multiple environments with the same services in them
this allows you to differentiate between them.

[Back to table](#table-nagios_context)


### proxy-extra-args


<a id="proxy-extra-args-description"> </a>
**Description:**

Space separated list of flags and key=value pairs that will be passed as arguments to
kube-proxy. For example a value like this:

```
  runtime-config=batch/v2alpha1=true profiling=true
```

will result in kube-apiserver being run with the following options:
  --runtime-config=batch/v2alpha1=true --profiling=true

[Back to table](#table-proxy-extra-args)


### snapd_refresh


<a id="snapd_refresh-description"> </a>
**Description:**

How often snapd handles updates for installed snaps. Setting an empty
string will check 4x per day. Set to "max" to delay the refresh as long
as possible. You may also set a custom string as described in the
'refresh.timer' section here:
  https://forum.snapcraft.io/t/system-options/87

[Back to table](#table-snapd_refresh)


### sysctl


<a id="sysctl-default"> </a>
**Default:**

```
{ net.ipv4.conf.all.forwarding : 1, net.ipv4.neigh.default.gc_thresh1 : 128, net.ipv4.neigh.default.gc_thresh2 : 28672, net.ipv4.neigh.default.gc_thresh3 : 32768, net.ipv6.neigh.default.gc_thresh1 : 128, net.ipv6.neigh.default.gc_thresh2 : 28672, net.ipv6.neigh.default.gc_thresh3 : 32768, fs.inotify.max_user_instances : 8192, fs.inotify.max_user_watches: 1048576 }
```


[Back to table](#table-sysctl)


<a id="sysctl-description"> </a>
**Description:**

YAML formatted associative array of sysctl values, e.g.:
'{kernel.pid_max : 4194303 }'. Note that kube-proxy handles
the conntrack settings. The proper way to alter them is to
use the proxy-extra-args config to set them, e.g.:

```
  juju config kubernetes-master proxy-extra-args="conntrack-min=1000000 conntrack-max-per-core=250000"
  juju config kubernetes-worker proxy-extra-args="conntrack-min=1000000 conntrack-max-per-core=250000"
```

The proxy-extra-args conntrack-min and conntrack-max-per-core can be set to 0 to ignore
kube-proxy's settings and use the sysctl settings instead. Note the fundamental difference between
the setting of conntrack-max-per-core vs nf_conntrack_max.

[Back to table](#table-sysctl)



<!-- CONFIG ENDS -->


## Actions

The kubernetes-worker charm models a few one time operations called
[Juju actions](https://jaas.ai/docs/working-with-actions) that can be run by
Juju users.

### Pause

Pausing the workload enables administrators to both drain and cordon
a unit for maintenance.

### Resume

Resuming the workload will uncordon a paused unit. Workloads will automatically
migrate unless otherwise directed via their application declaration.