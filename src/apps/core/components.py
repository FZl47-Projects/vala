from abc import ABC, abstractmethod
from django.template import loader, TemplateDoesNotExist
from django.contrib.auth import get_user_model
from django.http import HttpResponse

User = get_user_model()


class BaseComponentView(ABC):
    USER_ROLES = User.ALL_USER_ROLES
    CONTEXT_FUNC_ROLES = {
        'super_user': 'get_context_super_user',
        'operator_user': 'get_context_operator_user',
        'normal_user': 'get_context_normal_user',
    }

    template_name = None

    def get_template_by_user_role(self):
        user = self.request.user
        try:
            return loader.get_template(f"{self.BASE_DIR_TEMPLATE_COMPONENTS}/{user.role}/{self.template_name}")
        except TemplateDoesNotExist:
            try:
                return loader.get_template(f"{self.BASE_DIR_TEMPLATE_COMPONENTS}/base/{self.template_name}")
            except:
                pass
        raise FileNotFoundError(
            "template not found in component and base folder '%s' for '%s'" % (
                self.template_name, user.role))

    def get_context_by_user_role(self, *args, **kwargs):
        user = self.request.user
        context_func_name = self.CONTEXT_FUNC_ROLES.get(user.role, None)
        context_callable = getattr(self, context_func_name, None)
        try:
            return context_callable(*args, **kwargs)
        except NotImplementedError:
            try:
                return self.get_base_context(*args, **kwargs)
            except NotImplementedError:
                pass
        return {}

    @property
    @abstractmethod
    def BASE_DIR_TEMPLATE_COMPONENTS(self):
        pass

    def get_context_super_user(self, *args, **kwargs):
        raise NotImplementedError

    def get_context_operator_user(self, *args, **kwargs):
        raise NotImplementedError

    def get_context_normal_user(self, *args, **kwargs):
        raise NotImplementedError

    def get_base_context(self, *args, **kwargs):
        raise NotImplementedError

    def get(self, request, *args, **kwargs):
        template = self.get_template_by_user_role()
        context = self.get_context_by_user_role(*args, **kwargs)
        return HttpResponse(template.render(context, request), content_type="application/xhtml+xml")
