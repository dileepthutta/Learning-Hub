# FLASK WTForms

A form created using flask wtforms in python which is rendered using jinja.

---

## Description of this file.
1. Recently we have created a forms using html ,instead we can use wtforms.
2. Now to create forms using Python we need to create a class and pass a parameter FlaskForm
3. And create a variable = type of field(labelName)  Eg : password = PasswordField('Password') 
4. Create object and use the specific label and render it to the html file.
5. Now in that html file use Jinja templating to use. Eg: {{form.username.label}} {{form.username}}

---

### Why WTForms
- Easily we can handle forms
- Form validation can be done easily. And more.