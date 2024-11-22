from flask import Blueprint ,render_template, request

views = Blueprint(__name__ ,'views'   )

@views.route('/' )
def home():
    return render_template('Terms.html')
@views.route('/base' )
def base():
    return render_template('base.html', title="000" )

@views.route('/Privacy-Policy')
def PrivacyPolicy():
    return render_template('Privacy-Policy.html')

@views.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        message = request.form.get('message')
        # Handle form submission (e.g., send an email or save to a database)
        return render_template('contact.html', success=True)
    return render_template('contact.html', success=False)