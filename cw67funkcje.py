
def has_required_skills(person, skills):
    return all([skill in person['skills'] for skill in skills])


person1 = {'name':'John Doe', 'age':30, 'skills':['Python', 'Java', 'C++']}
person2 = {'name':'Jebac Policje', 'age':22, 'skills':['Python', 'C++']}

print(has_required_skills(person1, skills = ['Java', 'Python']))
