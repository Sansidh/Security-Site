from django import forms

class MD5Form(forms.Form):
    input = forms.CharField(label='Input', max_length=100)
    hashed = forms.CharField(label='Output', disabled = True)

    def process(self):
        cd = self.cleaned_data
        result = hashlib.md5()
        result.update(cd.input.encode('utf-8'))
        output = result.hexdigest()
        return output



