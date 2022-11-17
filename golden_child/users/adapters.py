from allauth.account.adapter import DefaultAccountAdapter

class CustomAccountAdapter(DefaultAccountAdapter):

    def save_user(self, request, user, form, commit=True):
        data = form.cleaned_data
        # 기본 저장 필드: first_name, last_name, username, email
        user = super().save_user(request, user, form, False)
        # 추가 저장 필드: profile_image
        is_parent = data.get("is_parent")
        if is_parent:
            user.is_parent = is_parent
        
        is_child = data.get("is_child")
        if is_child:
            user.is_child = is_child

        user.save()
        return user