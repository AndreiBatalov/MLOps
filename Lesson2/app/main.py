from models.user import User
import uvicorn

new_user = User(1, 'Bob123', 'Robert', 'Williams', '07.06.2000', 'male')
new_user.set_password('BobsPassword1234')
print(new_user.get_data())

if __name__ == '__main__':
    uvicorn.run('main:app', host='0.0.0.0', port = 8080, reload = True)