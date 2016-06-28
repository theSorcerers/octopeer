from rest_framework import serializers


class MultiKeyHyperlinkedIdentityField(serializers.HyperlinkedIdentityField):
    identity_args = {}
    def get_url(self, obj, view_name, request, format):
        if obj.pk is None:
            return None
        kwargs = dict((url_kw, getattr(obj, prop)) for url_kw, prop in self.identity_args.items())
        return self.reverse(view_name, kwargs=kwargs, request=request, format=format)

class UserHyperLinkedIdentityField(MultiKeyHyperlinkedIdentityField):
    identity_args = {
        'username': 'username',
    }

class RepositoryHyperlinkedIdentityField(MultiKeyHyperlinkedIdentityField):
    identity_args = {
        'owner': 'owner',
        'name': 'name'
    }

class PullRequestHyperlinkedIdentityField(serializers.HyperlinkedIdentityField):
    def get_url(self, obj, view_name, request, format):
        if obj.pk is None:
            return None
        repository = getattr(obj, 'repository')
        kwargs = {
            'owner': getattr(repository, 'owner'),
            'name': getattr(repository, 'name'),
            'pull_request_number': getattr(obj, 'pull_request_number')
        }
        return self.reverse(view_name, kwargs=kwargs, request=request, format=format)

class SessionHyperlinkedIdentityField(serializers.HyperlinkedIdentityField):
    def get_url(self, obj, view_name, request, format):
        if obj.pk is None:
            return None
        print(obj)
        pull_request = getattr(obj, 'pull_request')
        repository = getattr(pull_request, 'repository')
        user = getattr(obj, 'user')
        kwargs = {
            'username': getattr(user, 'username'),
            'owner': getattr(repository, 'owner'),
            'name': getattr(repository, 'name'),
            'pull_request_number': getattr(pull_request, 'pull_request_number')
        }
        return self.reverse(view_name, kwargs=kwargs, request=request, format=format)
