from flask import Flask, request, redirect,render_template,session,url_for,flash
import flask_excel as excel
import pyxlsb
import mysql.connector

import io


app = Flask(__name__)
app.secret_key = "super secret key"
excel.init_excel(app)

mydb=mysql.connector.connect(host="localhost",user="root",password="password",db="feedback")
cursor=mydb.cursor()





@app.route('/')
def home():
    return render_template('home.html')

@app.route('/adminlogin', methods=["GET", "POST"])
def adminlogin():
    msg=''
    #Getting the form data
    if request.method == 'POST':
        ad1 = request.form['username']
        bd1 = request.form['password']
        #sql Query to fetch the data according to the user input
        result=cursor.execute("select * from adt where username=%s and password=%s",[ad1,bd1])
        record = cursor.fetchone()#Fetching the data
        #Checking the user is valid or not. If User is valid then it is redirected to the Student view
        if record:
            session['loggedin']=True
            session['username']=record[0]
            session['shf']=''
            session['shfc']=''
            return redirect(url_for('adminview'))
        elif not record:
            return render_template('adminlogin.html',message='Invalid Username/Password')  
    return render_template('adminlogin.html')

@app.route('/studentlogin', methods=["GET", "POST"])
def studentlogin():
    msg=''
    #Getting the form data
    if request.method == 'POST':
        a1 = request.form['Rollnumber']
        b1 = request.form['password']
        #sql Query to fetch the data according to the user input
        result=cursor.execute("select * from stdata where rollno=%s and password=%s",(a1,b1))
        record = cursor.fetchone()#Fetching the data
        #Checking the user is valid or not. If User is valid then it is redirected to the Student view
        if record:
            session['loggedin']=True
            session['username']=record[0]
            print(session.get('username'))
            return redirect(url_for('studentview'))
        elif not record:
            return render_template('StudentLogin.html',message='Invalid Username/Password')
        
    return render_template('StudentLogin.html')

@app.route('/studentview')
def studentview():
    return render_template('student_view.html')

@app.route('/feedback',methods=['GET','POST'])
def feedback():
    if request.method == 'POST':

        user=str(session.get('username')+'feedback')
        com=session.get('username')+'comments'
        a='os'
        b='wt'
        c='flat'
        d='ps'
        e='se'

        aa1=request.form.get('a1');aa2=request.form.get('a2');aa3=request.form.get('a3');aa4=request.form.get('a4');aa5=request.form.get('a5')
        ba1=request.form.get('b1');ba2=request.form.get('b2');ba3=request.form.get('b3');ba4=request.form.get('b4');ba5=request.form.get('b5')
        ca1=request.form.get('c1');ca2=request.form.get('c2');ca3=request.form.get('c3');ca4=request.form.get('c4');ca5=request.form.get('c5')
        da1=request.form.get('d1');da2=request.form.get('d2');da3=request.form.get('d3');da4=request.form.get('d4');da5=request.form.get('d5')
        ea1=request.form.get('e1');ea2=request.form.get('e2');ea3=request.form.get('e3');ea4=request.form.get('e4');ea5=request.form.get('e5')
        fa1=request.form.get('f1');fa2=request.form.get('f2');fa3=request.form.get('f3');fa4=request.form.get('f4');fa5=request.form.get('f5')
        ga1=request.form.get('g1');ga2=request.form.get('g2');ga3=request.form.get('g3');ga4=request.form.get('g4');ga5=request.form.get('g5')
        ha1=request.form.get('h1');ha2=request.form.get('h2');ha3=request.form.get('h3');ha4=request.form.get('h4');ha5=request.form.get('h5')
        ia1=request.form.get('i1');ia2=request.form.get('i2');ia3=request.form.get('i3');ia4=request.form.get('i4');ia5=request.form.get('i5')
        ja1=request.form.get('j1');ja2=request.form.get('j2');ja3=request.form.get('j3');ja4=request.form.get('j4');ja5=request.form.get('j5')

        print(type(aa1))


        comment=request.form.get('comments')
        a1=1

        r1=f"update {user} set {a}='{aa1}',{b}='{aa2}',{c}='{aa3}',{d}='{aa4}',{e}='{aa5}'  where sno='1'"
        r2=f"update {user} set {a}='{ba1}' ,{b}='{ba2}',{c}='{ba3}',{d}='{ba4}',{e}='{ba5}'  where sno='2'"
        r3=f"update {user} set {a}='{ca1}' ,{b}='{ca2}',{c}='{ca3}',{d}='{ca4}',{e}='{ca5}'  where sno='3'"
        r4=f"update {user} set {a}='{da1}' ,{b}='{da2}',{c}='{da3}',{d}='{da4}',{e}='{da5}'  where sno='4'"
        r5=f"update {user} set {a}='{ea1}' ,{b}='{ea2}',{c}='{ea3}',{d}='{ea4}',{e}='{ea5}'  where sno='5'"
        r6=f"update {user} set {a}='{fa1}' ,{b}='{fa2}',{c}='{fa3}',{d}='{fa4}',{e}='{fa5}'  where sno='6'"
        r7=f"update {user} set {a}='{ga1}' ,{b}='{ga2}',{c}='{ga3}',{d}='{ga4}',{e}='{ga5}'  where sno='7'"
        r8=f"update {user} set {a}='{ha1}' ,{b}='{ha2}',{c}='{ha3}',{d}='{ha4}',{e}='{ha5}'  where sno='8'"
        r9=f"update {user} set {a}='{ia1}' ,{b}='{ia2}',{c}='{ia3}',{d}='{ia4}',{e}='{ia5}'  where sno='9'"
        r10=f"update {user} set {a}='{ja1}' ,{b}='{ja2}',{c}='{ja3}',{d}='{ja4}',{e}='{ja5}'  where sno='10'"

        result1=cursor.execute(r1)
        result2=cursor.execute(r2)
        result3=cursor.execute(r3)
        result4=cursor.execute(r4)
        result5=cursor.execute(r5)
        result6=cursor.execute(r6)
        result7=cursor.execute(r7)
        result8=cursor.execute(r8)
        result9=cursor.execute(r9)
        result10=cursor.execute(r10)

        commrec=cursor.execute(f"update {com} set comments='{comment}' where sno='{a1}'")
        mydb.commit()
        
        
    return render_template('feedback.html')
@app.route('/Adminview')
def adminview():
    return render_template('adminview.html')

@app.route('/logo')
def logo():
    return render_template('logo.html')

@app.route('/leftmenu')
def leftmenu():
    return render_template('leftmenu.html')

@app.route('/centerbox')
def centerbox():
    return render_template('centerbox.html')

@app.route('/rightmenu')
def rightmenu():
    return render_template('rightmenu.html')    

@app.route('/addform',methods=["GET", "POST"])
def addform():
    msg=''
    #Getting the form data
    if request.method == 'POST':
        a1 = request.form['rollnumber']
        b1 = request.form['branch']
        c1 ='123456'
        cursor.execute('select count(*) from stdata where rollno=%s',[a1])
        count=cursor.fetchone()[0]
        if count==1:
            cursor.close()
            flash('You are already registerterd!')
            return redirect(url_for('addform'))
        else:
            result=cursor.execute("insert into stdata values(%s,%s,%s)",(a1,c1,b1))
            mydb.commit()
        #sql Query to fetch the data according to the user input
        result=cursor.execute("insert into stdata values(%s,%s,%s)",(a1,c1,b1))
        #record = result.fetchone()#Fetching the data
        #Checking the user is valid or not. If User is valid then it is redirected to the Student view
        '''if record:
            session['loggedin']=True
            session['username']=record[0]
            return redirect(url_for('studentview'))
        else:
            msg='Incorrect username/password'  '''
        flash('Student Added Successfully!!')
        mydb.commit()
    return render_template('addform.html',msg=msg)

@app.route('/updateform',methods=["GET", "POST"])
def updateform():
    msg=''
    #Getting the form data
    if request.method == 'POST':
        a1 = request.form['rollnumber']
        b1 = request.form['branch']
        c1 = request.form['Newpassword']
        cursor.execute('select count(*) from stdata where rollno=%s',[a1])
        count=cursor.fetchone()[0]
        if count==1:
            result=cursor.execute("update stdata set password=%s where rollno=%s ",(c1,a1))
        else:
            flash('No student found with Entered Rollno')
            return redirect(url_for('updateform'))
        #sql Query to fetch the data according to the user input
        
        #record = result.fetchone()#Fetching the data
        #Checking the user is valid or not. If User is valid then it is redirected to the Student view
        '''if record:
            session['loggedin']=True
            session['username']=record[0]
            return redirect(url_for('studentview'))
        else:
            msg='Incorrect username/password'  '''
        mydb.commit()
    return render_template('updateform.html')

@app.route('/showstudent',methods=["GET", "POST"])
def showstudent():
    if request.method == 'POST':
        a1 = request.form['branch']
        #sql Query to fetch the data according to the User Input
        result=cursor.execute("select rollno,branch from stdata where branch=%s",([a1]))
        record=cursor.fetchall()
        return render_template('showstudentdata.html',value=record)


    return render_template('showstudent.html')

@app.route('/deletestudent',methods=["GET", "POST"])
def deletestudent():
    msg=''
    #Getting the form data
    if request.method == 'POST':
        a1 = request.form['rollnumber']
        b1 = request.form['branch']
        #sql Query to fetch the data according to the user input
        
        result=cursor.execute("delete from stdata where rollno=%s",([a1]))
        mydb.commit()
        #record = result.fetchone()#Fetching the data
        #Checking the user is valid or not. If User is valid then it is redirected to the Student view
        '''if record:
            session['loggedin']=True
            session['username']=record[0]
            return redirect(url_for('studentview'))
        else:
            msg='Incorrect username/password'  '''
        
    return render_template('deletestudent.html')

@app.route('/showfeedback',methods=["GET", "POST"])
def showfeedback():
    if request.method == 'POST':
        cursor=mydb.cursor(buffered=True)
        roll=request.form['rollnumber']
        a=roll+'feedback'
        b=roll+'comments'
        session['shf']=a
        session['shfc']=b
        result=cursor.execute(f"select {a}.sno,{a}.question,{a}.os,{a}.wt,{a}.flat,{a}.ps,{a}.se ,{b}.comments from {a} inner join {b} on {a}.sno={b}.sno")
        record=cursor.fetchall()
        if record:
            return render_template('showfeedbackdata.html',value=record)

    #result=cursor.execute("select * from feedback")
    #comre=cursor.execute("select comments from comments")
    
    
    return render_template('showfeedbackform.html')

@app.route('/resetfeedback',methods=["GET", "POST"])
def resetfeedback():
    cursor=mydb.cursor(buffered=True)
    a=session.get('shf')
    b=session.get('shfc')
    a1='os'
    b1='wt'
    c='flat'
    d='ps'
    e='se'
    a11='1'
    r1=f"update {a} set {a1}='{''}', {b1}='{''}',{c}='{''}',{d}='{''}',{e}='{''}'  where sno='1'"
    r2=f"update {a} set {a1}='{''}' ,{b1}='{''}',{c}='{''}',{d}='{''}',{e}='{''}'  where sno='2'"
    r3=f"update {a} set {a1}='{''}' ,{b1}='{''}',{c}='{''}',{d}='{''}',{e}='{''}'  where sno='3'"
    r4=f"update {a} set {a1}='{''}' ,{b1}='{''}',{c}='{''}',{d}='{''}',{e}='{''}'  where sno='4'"
    r5=f"update {a} set {a1}='{''}' ,{b1}='{''}',{c}='{''}',{d}='{''}',{e}='{''}'  where sno='5'"
    r6=f"update {a} set {a1}='{''}' ,{b1}='{''}',{c}='{''}',{d}='{''}',{e}='{''}'  where sno='6'"
    r7=f"update {a} set {a1}='{''}' ,{b1}='{''}',{c}='{''}',{d}='{''}',{e}='{''}'  where sno='7'"
    r8=f"update {a} set {a1}='{''}' ,{b1}='{''}',{c}='{''}',{d}='{''}',{e}='{''}'  where sno='8'"
    r9=f"update {a} set {a1}='{''}' ,{b1}='{''}',{c}='{''}',{d}='{''}',{e}='{''}'  where sno='9'"
    r10=f"update {a} set {a1}='{''}' ,{b1}='{''}',{c}='{''}',{d}='{''}',{e}='{''}'  where sno='10'"

    result1=cursor.execute(r1)
    result2=cursor.execute(r2)
    result3=cursor.execute(r3)
    result4=cursor.execute(r4)
    result5=cursor.execute(r5)
    result6=cursor.execute(r6)
    result7=cursor.execute(r7)
    result8=cursor.execute(r8)
    result9=cursor.execute(r9)
    result10=cursor.execute(r10)

    commrec=cursor.execute(f"update {b} set comments='{''}' where sno='{a11}'")
    mydb.commit()

    
    return render_template('resetfeedback.html')

@app.route('/addadmin',methods=["GET", "POST"])
def addadmin():
    msg=''
    #Getting the form data
    if request.method == 'POST':
        ad1 = request.form['username']
        bd1 = request.form['password']
        #sql Query to fetch the data according to the user input
        result=cursor.execute("insert into adt values(%s,%s)",(ad1,bd1))
        #record = result.fetchone()#Fetching the data
        
        
        mydb.commit()
    return render_template('addadmin.html')


@app.route('/download',methods=["GET","POST"])
def download():
    cursor=mydb.cursor(buffered=True)
    a=session.get('shf')
    b=session.get('shfc')
    c='comments'
    d=f"select {c} from {b}"
    
    cursor.execute(f"select * from {a}")
    data1=cursor.description
    lst=[i[0] for i in data1]
    cursor.execute(d)
    data2=cursor.description
    lst1=[i[0] for i in data2]
    cursor.execute(f"select {a}.sno,{a}.question,{a}.os,{a}.wt,{a}.flat,{a}.ps,{a}.se ,{b}.comments from {a} inner join {b} on {a}.sno={b}.sno")
    data=[list(i) for i in cursor.fetchall()]
    data.insert(0,lst+lst1)
    #return (data)
    return excel.make_response_from_array(data, "xlsm",file_name=f"{a}_report")


@app.route('/studentlogout',methods=["GET","POST"])
def studentlogout():
    if session.get['username']:
        session.pop('username')
        return redirect(url_for('home'))
    

@app.route('/adminlogout',methods=["GET","POST"])
def adminlogout():
    if session.get['username']:
        session.pop('username')
        return redirect(url_for('home'))
    return redirect(url_for('home'))






if __name__ == '__main__':
    app.run(debug=True)
