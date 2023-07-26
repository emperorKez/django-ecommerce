# from django import forms
# from core.models import Product, Category, ProductImage



# class ProductForm():
    
#     class Meta:
#         model = Product
#         fields = ['firstname', 'lastname', 'password1','password2','email','street','city','state','country','phone_number','zip_code','is_subscribed']
#         widget = {
#             'firstname': forms.TextInput(attrs={'placeholder': 'First Name'}),
#             'firstname': forms.TextInput(attrs={'placeholder': 'First Name'}),
#             'email': forms.TextInput(attrs={'placeholder': 'Email'}),
#             'street': forms.TextInput(attrs={'placeholder': 'Street'}),
#             'city': forms.TextInput(attrs={'placeholder': 'City'}),
#             'country': forms.TextInput(attrs={'placeholder': 'Country'}),
#             'phone_number': forms.TextInput(attrs={'placeholder': 'Phone Number'}),
#             'zip_code': forms.TextInput(attrs={'placeholder': 'Zip Code'}),
#             'password1': forms.TextInput(attrs={'placeholder': 'Password'}),
#             'password2': forms.TextInput(attrs={'placeholder': 'Confirm Password'}),
#         }
        
# class LoginForm():
    
#     class Meta:
#         model = User
#         fields = ['email', 'password'] 
  


# class ProductImageForm(forms.ModelForm):
#     class Meta:
#         model = ProjectImage
#         fields = ['title', 'describtion', 'images']
#         widgets = {
#             'images': forms.ClearableFileInput(attrs={'multiple': True}),
#         }     





# views.py

# def createProject(request):
#     form = ProjectForm(instance=ProjectImage)

#     if request.method == 'POST':
#         form = ProjectForm(request.POST, request.FILES.getlist('image'))
#         if form.is_valid():
#             project = form.save(commit=False)
#             project.save()
#     context = {'form':form}
#     return render(request, 'projects/project_form.html', context)
# Instances are pretty new to me, so sorry for what I just send to you 