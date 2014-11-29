# Django Class-Based Admin


## What is `django-cba`

`django-cba` aims to be an unofficial replacement for Django's (fantastic)
admin interface, builing upon class-based views, and making use of the
app-loading refactor made available in Django 1.7.


## Why is a replacement needed?

The existing system does the job admirably. Realistically, a replacement is
probably not *needed*.

That said, while the existing admin interface is very good, it can
be hard to heavily customise. I have been drooling over the idea of a
class-based admin interface for too long. Rather than continue to wait for it,
I have decided to give it a shot myself


## What is the state of this project?

Frankly, it's still at the "just a dream" stage at the moment. I'm writing this
mainly as a way to collect my thoughts and lay out my intentions.

Also, yes I know that the name is silly. It may change. Don't hold your breath.


## What's on the roadmap?

I would like to produce a system that caters for the majority (if not all) of
the use cases of Django's admin.

I do not have an exhaustive list of them, so, in no particular order, I would
like to achieve:


### MVP

- [ ] **Model registration using app loading.** This means that there will be
no need to unregister models from third-party apps in order to override them.
Instead, one can simply define a new app config.
- [ ] **Customisable templates.** If you need to add something simple to a
view or change the styles, then the templates should be written to allow for
this as much as sensible.
- [ ] **Customisable views.** Django's class-based views were designed with
extension in mind. It should be trivial to extend or replace them.
 - [ ] For a model.
 - [ ] For an app.
 - [ ] For all apps.
- [ ] **Customisable URLs.** If replacing the views is not enough, it will be
possible to use custom urls:
 - [ ] For a model.
 - [ ] For an app.
 - [ ] For all apps.
- [ ] **Access permissions.** As with Django's admin, it will be great to
distinguish between Users with `is_staff` and Users with `is_superuser`.


### Future

- [ ] **Inline related models.** As with Django's admin, it will be beneficial
to allow models to be edited/created alongside another (eg. Creating `Choice`s
on the same page as a `Poll`.). This may be a little complex, so rather than
delay progress, this can come in a later version.


## Anything else?

At the same time, I would like to focus on:

- **Minimal external dependencies.** Though this may prove impractical in tests.
- **Maintaining 100% test coverage** ...yet understanding that coverage doesn't
ensure perfect code.
- **High code standards.** I like PEP8, PEP257, and google's import order.
I do not like `#noqa`.
- **Security.** If you discover a security issue, please refrain from opening
an issue/making a pull request. Instead, please email me: <charlie@meshy.co.uk>.
