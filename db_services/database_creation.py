import MySQLdb
import datetime
from copy import deepcopy

import start_db
import edit_user
import edit_friendships
import edit_posts


db = start_db.launchdb()
cursor = start_db.launchcursor(db)    

####### Insert User ########


# user_id = cursor.lastrowid
# start_time = datetime.datetime.now()
# bday = '2016-05-09'
# car = edit_user.user(user_id, 'Cardy', 'Wei', 'cwei3', 'cardywei', '', '5V ground', 'UNDERWATER DOLPHIN CHARMER', bday, 'wei@cooper.edu', start_time, 1)

# user_id = cursor.lastrowid
# start_time = datetime.datetime.now()
# jas = edit_user.user(user_id, 'Jasmine', 'Tang', 'jtangqt', 'jasminetang', '', 'Friends dont harrass other friends.', 'supermodel', bday, 'tang@cooper.edu', start_time, 1)

# user_id = cursor.lastrowid
# start_time = datetime.datetime.now()
# sam = edit_user.user(user_id, 'sam', 'cheng', 'scheng829', 'samcheng', '', 'Watch my dance moves', 'professional dancer', bday, 'scheng839@gmail.com', start_time, 1)

# user_id = cursor.lastrowid
# start_time = datetime.datetime.now()
# alex = edit_user.user(user_id, 'alex', 'hu', 'enigmamemory', 'alexhu', '', 'AHH NLP', 'cooper union student', bday,'hu5@cooper.edu', start_time, 1)

# user_id = cursor.lastrowid
# start_time = datetime.datetime.now()
# kc = edit_user.user(user_id, 'casey', 'he', 'squishybluewristbutt', 'caseyhe', '', 'ROCK CLIMBING', 'ALIVE', bday,'he@cooper.edu', start_time, 1)

# user_id = cursor.lastrowid
# start_time = datetime.datetime.now()
# joey = edit_user.user(user_id, 'joey', 'benghaasllkfdldaflaf', 'tritus', 'joey', '', '@everyone, league???', 'miner in data', bday,'jbengtlfdf15@gmail.com', start_time, 1)

# user_id = cursor.lastrowid
# start_time = datetime.datetime.now()
# jerry = edit_user.user(user_id, 'jeremiah', 'pratt', 'sabooap', 'jeremiahpratt', '', 'Again, our sincere apologies to the families who went home disappointed.', 'politician', bday, 'pratt@cooper.edu', start_time, 1)

# user_id = cursor.lastrowid
# start_time = datetime.datetime.now()
# dan = edit_user.user(user_id, 'dan', 'park', 'solarien', 'danpark', '', 'Join the army with me!', 'General of the ONE Korean Army', bday, 'park100000@cooper.edu', start_time, 1)

# user_id = cursor.lastrowid
# start_time = datetime.datetime.now()
# dk = edit_user.user(user_id, 'dongkyu', 'kim', 'dongkyu0419', 'dongkyukim', '', 'TRIVIAL', 'Professor Kirtman :POGGERS:', bday, 'kim800@cooper.edu', start_time, 1)

# user_id = cursor.lastrowid
# start_time = datetime.datetime.now()
# minyoung = edit_user.user(user_id, 'minyoung', 'na', 'BSEintruder', 'minyuongna', '', 'REEEEEEEEEEEEE', 'i want to be a puppy', bday, 'na4@cooper.edu', start_time, 1)

# user_id = cursor.lastrowid
# start_time = datetime.datetime.now()
# bri = edit_user.user(user_id, 'brian', 'hong', 'th0m4s', 'brianhong', '', '66k+ groups', 'thomas', bday, 'bri@cooper.edu', start_time, 1)

# user_id = cursor.lastrowid
# start_time = datetime.datetime.now()
# paul = edit_user.user(user_id, 'paul', 'kang', 'cheeseheadpk', 'paulkang', '', 'I own a burger joint', 'Construction Worker/Bob the Builder', bday, 'kang3@cooper.edu', start_time, 1)

# user_id = cursor.lastrowid
# start_time = datetime.datetime.now()
# chris = edit_user.user(user_id, 'chris', 'watkins', 'WATGOIN', 'chriswatkins', '', 'I am a front end developer', 'full stack developer', bday, 'watkins@cooper.edu', start_time, 1)


# edit_user.insert_u(cursor, car)
# edit_user.insert_u(cursor, jas)
# edit_user.insert_u(cursor, sam)
# edit_user.insert_u(cursor, alex)
# edit_user.insert_u(cursor, kc)
# edit_user.insert_u(cursor, joey)
# edit_user.insert_u(cursor, jerry)
# edit_user.insert_u(cursor, dan)
# edit_user.insert_u(cursor, dk)
# edit_user.insert_u(cursor, minyoung)
# edit_user.insert_u(cursor, bri)
# edit_user.insert_u(cursor, paul)
# edit_user.insert_u(cursor, chris)


# # ###### Insert Friendships #######


# edit_friendships.add_f(cursor, 'scheng829', 'jtangqt')
# edit_friendships.add_f(cursor, 'sabooap', 'enigmamemory')
# edit_friendships.add_f(cursor, 'tritus', 'jtangqt')
# edit_friendships.add_f(cursor, 'squishybluewristbutt','jtangqt')
# edit_friendships.add_f(cursor, 'enigmamemory', 'cwei3')
# edit_friendships.add_f(cursor, 'dongkyu0419','jtangqt')
# edit_friendships.add_f(cursor, 'solarien','jtangqt')
# edit_friendships.add_f(cursor, 'tritus', 'sabooap')
# edit_friendships.add_f(cursor, 'cwei3', 'jtangqt')
# edit_friendships.add_f(cursor, 'sabooap', 'tritus')
# edit_friendships.add_f(cursor, 'dongkyu0419', 'th0m4s')
# edit_friendships.add_f(cursor, 'sabooap', 'solarien')
# edit_friendships.add_f(cursor, 'enigmamemory', 'scheng829')
# edit_friendships.add_f(cursor, 'cheeseheadpk', 'WATGOIN') 
# edit_friendships.add_f(cursor, 'BSEintruder', 'dongkyu0419')
# edit_friendships.add_f(cursor, 'cwei3', 'tritus')
# edit_friendships.add_f(cursor, 'solarien', 'BSEintruder')
# edit_friendships.add_f(cursor, 'WATGOIN', 'sabooap')
# edit_friendships.add_f(cursor, 'th0m4s', 'cheeseheadpk')

# edit_friendships.confirm_f(cursor, 'scheng829', 'jtangqt', 1)
# edit_friendships.confirm_f(cursor, 'sabooap', 'enigmamemory', 1)
# edit_friendships.confirm_f(cursor, 'tritus', 'jtangqt', 1)
# edit_friendships.confirm_f(cursor, 'squishybluewristbutt','jtangqt', 1)
# edit_friendships.confirm_f(cursor, 'enigmamemory', 'cwei3', 1)
# edit_friendships.confirm_f(cursor, 'dongkyu0419','jtangqt', 1)
# edit_friendships.confirm_f(cursor, 'solarien','jtangqt', 1)
# edit_friendships.confirm_f(cursor, 'tritus', 'sabooap', 1)
# edit_friendships.confirm_f(cursor, 'cwei3', 'jtangqt', 1)
# # edit_friendships.confirm_f(cursor, 5, 2, 1)
# # edit_friendships.confirm_f(cursor, 8, 2, 1)
# # edit_friendships.confirm_f(cursor, 9, 2, 1)



# ###### Insert Posts #######

# post_time = datetime.datetime.now()
# post_id = cursor.lastrowid
# post1 = edit_posts.post(post_id, 'scheng829', 'jtangqt', post_time, 'once upon a time')
# post_time = datetime.datetime.now()
# post_id = cursor.lastrowid
# post2 = edit_posts.post(post_id, 'cwei3', 'cwei3', post_time, 'there was a person')
# post_time = datetime.datetime.now()
# post_id = cursor.lastrowid
# post3 = edit_posts.post(post_id, 'sabooap', 'enigmamemory', post_time, 'who wanted to eat ')
# post_time = datetime.datetime.now()
# post_id = cursor.lastrowid
# post4 = edit_posts.post(post_id, 'tritus', 'jtangqt', post_time, 'cup noooooodles all the time')
# post_time = datetime.datetime.now()
# post_id = cursor.lastrowid
# post5 = edit_posts.post(post_id, 'squishybluewristbutt','jtangqt', post_time, 'and his name was........ exdee')
# post_time = datetime.datetime.now()
# post_id = cursor.lastrowid
# post6 = edit_posts.post(post_id, 'enigmamemory','enigmamemory', post_time, 'and his name was........ exdee')
# post_time = datetime.datetime.now()
# post_id = cursor.lastrowid
# post7 = edit_posts.post(post_id, 'cwei3','enigmamemory', post_time, 'and his name was........ exdee')
# post_time = datetime.datetime.now()
# post_id = cursor.lastrowid
# post8 = edit_posts.post(post_id, 'dongkyu0419','jtangqt', post_time, 'and his name was........ exdee')
# post_time = datetime.datetime.now()
# post_id = cursor.lastrowid
# post9 = edit_posts.post(post_id, 'solarien','jtangqt', post_time, 'YA LIKE JAZZ?')
# post_time = datetime.datetime.now()
# post_id = cursor.lastrowid
# post10 = edit_posts.post(post_id, 'sabooap','enigmamemory', post_time, 'i know you do')
# post_time = datetime.datetime.now()
# post_id = cursor.lastrowid
# post11 = edit_posts.post(post_id, 'enigmamemory','cwei3', post_time, 'HEH')


# edit_posts.create_p(cursor, post1)
# edit_posts.create_p(cursor, post2)
# edit_posts.create_p(cursor, post3)
# edit_posts.create_p(cursor, post4)
# edit_posts.create_p(cursor, post5)
# edit_posts.create_p(cursor, post6)
# edit_posts.create_p(cursor, post7)
# edit_posts.create_p(cursor, post8)
# edit_posts.create_p(cursor, post9)
# edit_posts.create_p(cursor, post10)
# edit_posts.create_p(cursor, post11)


edit_friendships.delete_f(cursor, 1, 6)
edit_friendships.add_f(cursor, 'tritus', 'cwei3')

start_db.commitclose(cursor, db)