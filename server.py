import sqlalchemy
from sqlalchemy.orm import sessionmaker
from models import engine, User, Pet

Session = sessionmaker(bind=engine)

def main():
  session = Session()
  tosspot = User(name='Gavin Callandar', email='gavin.callandar@ga.co', nickname='Gav')
  session.add(tosspot)

  session.add_all([User(name='Wendy Williams', email='wendwil@gmail.com', nickname='Windy'),
                   User(name='Steven Peters', email='steven.peters@ga.co', nickname='Stevie'),
                   User(name='Mary Contrary', email='marycontrary@gmail.com', nickname='Mar'),
                   User(name='Michael Schull', email='mikeyboi@gmail.com', nickname='Mike'),
                   User(name='Madison Edminston', email='madison.edminston@ga.co', nickname='Mads')])
  go_to_gal = session.query(User).filter_by(nickname='Mads').first()
  # go_to_gal.email = 'madison.edminston@generalassemb.ly'
  # print(go_to_gal)
  # session.query(User).filter_by(nickname='Mar').delete()
  # session.delete(tosspot)
  # print(session.query(User).filter(User.nickname.in_(['Mar', 'Gav'])).count())
  go_to_gal.pets = [Pet(name='Emmy', species='dog', age=2)]
  print(go_to_gal.pets)
  print(session.query(User).filter_by(nickname='Mads').first().pets)
  go_to_gal.pets += [Pet(name='Ballad', species='dog', age=9), Pet(name='Blub', species='fish')]
  go_to_gal.pets[0].user
  print(go_to_gal)

  session.query(User, Pet).filter(User.id == Pet.user_id).filter(Pet.name == 'Emmy').all()

  session.query(User).join(Pet).filter(Pet.name == 'Emmy').all()
  print(session.query(User).filter_by(nickname='Mads').count())
  # -> 1
  print(session.query(Pet).filter(Pet.name.in_(['Emmy', 'Ballad', 'Blub'])).count())
  # -> 3

  # Delete Mads
  session.delete(go_to_gal)

  print(session.query(User).filter_by(nickname='Mads').count())
  # -> 0
  print(session.query(Pet).filter(Pet.name.in_(['Emmy', 'Ballad', 'Blub'])).count())
  # -> 0
  # emmy.toys.append(Toy(toy='ball'))
  # print("🎾", emmy.toys)
  # session.commit()
if __name__ == '__main__':
  main()