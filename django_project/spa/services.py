from user_profile.models import Profile


def profileCreate(profile_data,instance):
    name = profile_data.get('name')
    age = profile_data.get('age')
    email = profile_data.get('email')
    Profile.objects.create(name=name,age=age,email=email,user=instance)