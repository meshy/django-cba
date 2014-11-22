# Django Class-Based Admin

## What is `django-cba`

`django-cba` aims to be a replacement for Django's (fantastic) admin interface
built upon class-based views, and making use of the new app-loading refactor.

## Why is a replacement needed

Realistically, it's probably not needed. The existing system does the job
admirably. That said, while the existing admin interface is very good, it can
be hard to customise, and it's design is beginning to show it's age. I have
been drooling over the idea of a class- based admin interface for too long, so
I have decided to give it a shot. Also, it will mean that we can finally get
rid of that odd `admin.autodiscover()` once and for all.
