# Get user email address
email = input("What is your email address?: ").strip(".com")
list_name=email.split("@")
# Slice out the user name
user_name=list_name[0]

# Slice the domain name
domain_name=list_name[1]

# Format message
output = "Your username is '{}' and your domain name is '{}'".format(user_name,domain_name)

# Display output message
print(output)
email=input("input a email:")
list_email_fixed=email.split("@")

domain = {'gmail.com':'Google','yahoo.com.tw':'Yahoo','ntu.edu.tw':'臺大','hotmail.com.tw':'Hotmail','hotmail.com':'Hotmail'}

if list_email_fixed[1]=="gmail.com":
    output = "這是註冊在 {} 之下的 Email 地址'".format(domain["gmail.com"])
else:
    
    output = "這是在 {} 之下自定義域".format(domain[list_email_fixed[1]])
print(output)


