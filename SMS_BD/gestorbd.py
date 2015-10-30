#!/usr/bin/python3
# -*- coding: utf-8 -*-

import MySQLdb


class Alumno:

    def __init__(self):
        self.dni = ""
        self.nombre = ""

class Asignatura:

    def __init__(self):
        self.id = ""
        self.nombre = ""

class Profesor:

    def __init__(self):
        self.dni = ""
        self.nombre = ""
        self.apellidos = ""
        self.municipio = ""
        self.provincia = ""
        self.domicilio = ""
        self.email = ""
        self.telefono = ""

class Grupo:

    def __init__(self):
        self.curso = ""
        self.letra = ""

class Pertenece:

    def __init__(self):

        self.curso = ""
        self.letra = ""
        self.idAsignatura = ""
        '''
        self.grupo = Grupo()
        self.Asignatura = Asignatura()
        '''

class Imparte:

    def __init__(self):
        self.curso = ""
        self.letra = ""
        self.idAsignatura = ""
        self.dniProfesor = ""
        '''
        self.Profesor = Profesor()
        self.Pertenece = Pertenece()
        '''

class Cursa:

    def __init__(self):
        self.curso = ""
        self.letra = ""
        self.idAsignatura = ""
        self.dniAlumno = ""
        '''
        self.Alumno = Alumno()
        self.Pertenece = Pertenece()
        '''






class GestorAlumno:

    @classmethod
    def nuevoAlumno(self, dni, nombre):
        db = MySQLdb.connect(host="localhost", user="root", db="mdb")

        sel= "Select count(*) from Alumno where (dni ='"+str(dni)+"');"
        query="INSERT INTO Alumno values("+"'"+str(dni)+"', "+"'"+nombre+"');"

        cursor = db.cursor()

        cursor.execute(sel)
        existe=int(cursor.fetchone()[0])

        if existe==0:
        	cursor.execute(query)

        db.commit()
        cursor.close()
        db.close()

    @classmethod
    def getAlumnos(self):
        db = MySQLdb.connect(host="localhost", user="root", db="mdb");

        cursor = db.cursor()
        query="select * from Alumno";
        cursor.execute(query);
        row = cursor.fetchone()

        lista = []

        while row is not None:
            Alumno = Alumno()
            Alumno.dni=row[0]
            Alumno.nombre=row[1]
            lista.append(Alumno)
            #print row[0], row[1]
            row = cursor.fetchone()

        cursor.close()
        db.close()

        return lista

'''
    @classmethod
    def borrarAlumno(self, dnient):
        db = MySQLdb.connect(host="localhost", user="root", db="mdb"); #La conexión está clara.
        query="DELETE FROM Alumno WHERE dni="+dnient+";"
        cursor = db.cursor()
        cursor.execute(query);
        db.commit()
        cursor.close()
        db.close()
'''

class GestorAsignatura:

    @classmethod
    def nuevaAsignatura(self, id, nombre):
        db = MySQLdb.connect(host="localhost", user="root", db="mdb")

        sel= "Select count(*) from Asignatura where (id ='"+str(id)+"');"
        query="INSERT INTO Asignatura values("+"'"+str(id)+"', "+"'"+nombre+"');"

        cursor = db.cursor()

        cursor.execute(sel)
        existe=int(cursor.fetchone()[0])

        if existe==0:
            cursor.execute(query)

        db.commit()
        cursor.close()
        db.close()

    @classmethod
    def getAsignaturas(self):
        db = MySQLdb.connect(host="localhost", user="root", db="mdb");

        cursor = db.cursor()
        query="select * from Asignatura";
        cursor.execute(query);
        row = cursor.fetchone()

        lista = []

        while row is not None:
            Asignatura = Asignatura()
            Asignatura.id=row[0]
            Asignatura.nombre=row[1]
            lista.append(Asignatura)
            #print row[0], row[1]
            row = cursor.fetchone()

        cursor.close()
        db.close()

        return lista

'''
    @classmethod
    def borrarAsignatura(self, id):
        db = MySQLdb.connect(host="localhost", user="root", db="mdb"); #La conexión está clara.
        query="DELETE FROM Asignatura WHERE id="+id+";"
        cursor = db.cursor()
        cursor.execute(query);
        db.commit()
        cursor.close()
        db.close()
'''

class GestorProfesor:

    @classmethod
    def nuevoProfesor(self, dni, nombre, apellidos, municipio, provincia, domicilio, email, telefono):
        db = MySQLdb.connect(host="localhost", user="root", db="mdb")

        sel= "Select count(*) from Profesor where (dni ='"+str(dni)+"');"
        query="INSERT INTO Profesor values("+"'"+str(dni)+"', "+"'"+nombre+"', "+"'"+apellidos+"', "+"'"+municipio+"', "+"'"+provincia+"', "+"'"+domicilio+"', "+"'"+email+"', "+"'"+str(telefono)+"');"

        cursor = db.cursor()

        cursor.execute(sel)
        existe=int(cursor.fetchone()[0])

        if existe==0:
            cursor.execute(query)

        db.commit()
        cursor.close()
        db.close()

    @classmethod
    def getProfesores(self):
        db = MySQLdb.connect(host="localhost", user="root", db="mdb");

        cursor = db.cursor()
        query="select * from Profesor";
        cursor.execute(query);
        row = cursor.fetchone()

        lista = []

        while row is not None:
            Profesor = Profesor()
            Profesor.dni=row[0]
            Profesor.nombre=row[2]
            Profesor.apellidos=row[3]
            Profesor.municipio=row[4]
            Profesor.provincia=row[5]
            Profesor.domicilio=row[6]
            Profesor.email=row[7]
            Profesor.telefono=row[8]
            lista.append(Profesor)
            #print row[0], row[1]
            row = cursor.fetchone()

        cursor.close()
        db.close()

        return lista

'''
    @classmethod
    def borrarProfesor(self, id):
        db = MySQLdb.connect(host="localhost", user="root", db="mdb"); #La conexión está clara.
        query="DELETE FROM Profesor WHERE dni="+dni+";"
        cursor = db.cursor()
        cursor.execute(query);
        db.commit()
        cursor.close()
        db.close()
'''

class GestorGrupo:

    @classmethod
    def nuevoGrupo(self, id, nombre):
        db = MySQLdb.connect(host="localhost", user="root", db="mdb")

        sel= "Select count(*) from Grupo where (id ='"+str(curso)+"AND letra ='"+letra+"');"
        query="INSERT INTO Grupo values("+"'"+str(curso)+"', "+"'"+letra+"');"

        cursor = db.cursor()

        cursor.execute(sel)
        existe=int(cursor.fetchone()[0])

        if existe==0:
            cursor.execute(query)

        db.commit()
        cursor.close()
        db.close()

    @classmethod
    def getGrupos(self):
        db = MySQLdb.connect(host="localhost", user="root", db="mdb");

        cursor = db.cursor()
        query="select * from Grupo";
        cursor.execute(query);
        row = cursor.fetchone()

        lista = []

        while row is not None:
            Grupo = Grupo()
            Grupo.curso=row[0]
            Grupo.letra=row[1]
            lista.append(Grupo)
            #print row[0], row[1]
            row = cursor.fetchone()

        cursor.close()
        db.close()

        return lista

'''
    @classmethod
    def borrarGrupo(self, curso, letra):
        db = MySQLdb.connect(host="localhost", user="root", db="mdb"); #La conexión está clara.
        query="DELETE FROM Asignatura WHERE curso="+curso+"AND letra="+letra+";"
        cursor = db.cursor()
        cursor.execute(query);
        db.commit()
        cursor.close()
        db.close()
'''

class GestorPertenece:

    @classmethod
    def nuevaPertenencia(self, curso, letra, idAsignatura):
        db = MySQLdb.connect(host="localhost", user="root", db="mdb")
        gs=GestorUsuario()
        sel_c= "SELECT count(*) from Pertenece where curso ="+"'"+str(curso)+"' AND letra='"+letra+"';"
        sel_e= "SELECT count(*) from Asignatura where (id ="+"'"+str(idAsignatura)+"');"
        query="INSERT INTO Pertenece values("+"'"+str(curso)+"', '"+str(letra)+"', '"+str(idAsignatura)+"');"

        cursor = db.cursor()

        cursor.execute(sel_c)
        existe_c=int(cursor.fetchone()[0])
        cursor.execute(sel_e)
        existe_e=int(cursor.fetchone()[0])

        if existe_c==0 and existe_e>0:
        	gs.nuevoGrupo(curso, letra)
        	cursor.execute(query)

        db.commit()
        cursor.close()
        db.close()

    @classmethod
    def borrarPertenencia(self, curso, letra, dni):
        db = MySQLdb.connect(host="localhost", user="root", db="mdb")

        sel_c= "SELECT count(*) from Cursa where curso ="+"'"+str(curso)+"' AND letra='"+letra+"' and  idAsignatura='"+str(idAsignatura)+"';"
        query="DELETE FROM Cursa where where curso ="+"'"+str(curso)+"' AND letra='"+letra+"' and  idAsignatura='"+str(idAsignatura)+"';"

        cursor = db.cursor()


        cursor.execute(sel_c)
        existe_c=int(cursor.fetchone()[0])


        if existe_c>0 :
        	cursor.execute(query)

        db.commit()
        cursor.close()
        db.close()


    @classmethod
    def getPertenencias(self):
        db = MySQLdb.connect(host="localhost", user="root", db="mdb");

        cursor = db.cursor()
        query="select * from Pertenece";
        cursor.execute(query);
        row = cursor.fetchone()

        lista = []

        while row is not None:
            pertenece = Pertenece()
            pertenece.curso=row[0]
            pertenece.letra=row[1]
            pertenece.idAsignatura=row[2]
            lista.append(pertenece)
            #print row[0], row[1]
            row = cursor.fetchone()

        cursor.close()
        db.close()

        return lista

class GestorImparte:

    @classmethod
    def nuevaImparticion(self, curso, letra, idAsignatura, dniProfesor):
        db = MySQLdb.connect(host="localhost", user="root", db="mdb")
        gs=GestorUsuario()
        sel_c= "SELECT count(*) from Imparte where curso ="+"'"+str(curso)+"' AND letra='"+letra+"' and  idAsignatura='"+str(idAsignatura)+"', dniProfesor='"+str(dniProfesor)+"';"
        sel_e= "SELECT count(*) from Pertenece where (curso ="+"'"+str(curso)+"' AND letra='"+letra+"' AND idAsignatura ="+"'"+str(idAsignatura)+"');"
        sel_g= "SELECT count(*) from Profesor where (dni="+"'"+str(dniProfesor)+"');"
        query="INSERT INTO Imparte values("+"'"+str(curso)+"', '"+str(letra)+"', '"+str(idAsignatura)+"', '"+str(dniProfesor)+"');"

        cursor = db.cursor()

        cursor.execute(sel_c)
        existe_c=int(cursor.fetchone()[0])
        cursor.execute(sel_e)
        existe_e=int(cursor.fetchone()[0])
        cursor.execute(sel_g)
        existe_g=int(cursor.fetchone()[0])

        if existe_c==0 and existe_e>0 and existe_g>0:
            cursor.execute(query)

        db.commit()
        cursor.close()
        db.close()

    @classmethod
    def borrarImparticion(self, curso, letra, idAsignatura, dniProfesor):
        db = MySQLdb.connect(host="localhost", user="root", db="mdb")

        sel_c= "SELECT count(*) from Imparte where curso ="+"'"+str(curso)+"' AND letra='"+letra+"' and  idAsignatura='"+str(idAsignatura)+"', dniProfesor='"+str(dniProfesor)+"';"
        query="DELETE FROM Imparte where where curso ="+"'"+str(curso)+"' AND letra='"+letra+"' and  idAsignatura='"+str(idAsignatura)+"', dniProfesor='"+str(dniProfesor)+"';"

        cursor = db.cursor()


        cursor.execute(sel_c)
        existe_c=int(cursor.fetchone()[0])


        if existe_c>0 :
            cursor.execute(query)

        db.commit()
        cursor.close()
        db.close()


    @classmethod
    def getImparticiones(self):
        db = MySQLdb.connect(host="localhost", user="root", db="mdb");

        cursor = db.cursor()
        query="select * from Imparte";
        cursor.execute(query);
        row = cursor.fetchone()

        lista = []

        while row is not None:
            imparte = Imparte()
            imparte.curso=row[0]
            imparte.letra=row[1]
            imparte.idAsignatura=row[2]
            imparte.dniProfesor=row[3]
            lista.append(imparte)
            #print row[0], row[1]
            row = cursor.fetchone()

        cursor.close()
        db.close()

        return lista


class GestorCursa:

    @classmethod
    def nuevoCurso(self, curso, letra, idAsignatura, dniAlumno):
        db = MySQLdb.connect(host="localhost", user="root", db="mdb")
        gs=GestorUsuario()
        sel_c= "SELECT count(*) from Cursa where curso ="+"'"+str(curso)+"' AND letra='"+letra+"' and  idAsignatura='"+str(idAsignatura)+"', dniAlumno='"+str(dniAlumno)+"';"
        sel_e= "SELECT count(*) from Pertenece where (curso ="+"'"+str(curso)+"' AND letra='"+letra+"' AND idAsignatura ="+"'"+str(idAsignatura)+"');"
        sel_g= "SELECT count(*) from Alumno where (dni="+"'"+str(dniAlumno)+"');"
        query="INSERT INTO Cursa values("+"'"+str(curso)+"', '"+str(letra)+"', '"+str(idAsignatura)+"', '"+str(dniAlumno)+"');"

        cursor = db.cursor()

        cursor.execute(sel_c)
        existe_c=int(cursor.fetchone()[0])
        cursor.execute(sel_e)
        existe_e=int(cursor.fetchone()[0])
        cursor.execute(sel_g)
        existe_g=int(cursor.fetchone()[0])

        if existe_c==0 and existe_e>0 and existe_g>0:
            cursor.execute(query)

        db.commit()
        cursor.close()
        db.close()

    @classmethod
    def borrarCurso(self, curso, letra, idAsignatura, dniAlumno):
        db = MySQLdb.connect(host="localhost", user="root", db="mdb")

        sel_c= "SELECT count(*) from Cursa where curso ="+"'"+str(curso)+"' AND letra='"+letra+"' and  idAsignatura='"+str(idAsignatura)+"', dniAlumno='"+str(dniAlumno)+"';"
        query="DELETE FROM Cursa where where curso ="+"'"+str(curso)+"' AND letra='"+letra+"' and  idAsignatura='"+str(idAsignatura)+"', dniAlumno='"+str(dniAlumno)+"';"

        cursor = db.cursor()


        cursor.execute(sel_c)
        existe_c=int(cursor.fetchone()[0])


        if existe_c>0 :
            cursor.execute(query)

        db.commit()
        cursor.close()
        db.close()


    @classmethod
    def getCursos(self):
        db = MySQLdb.connect(host="localhost", user="root", db="mdb");

        cursor = db.cursor()
        query="select * from Cursa";
        cursor.execute(query);
        row = cursor.fetchone()

        lista = []

        while row is not None:
            cursa = Cursa()
            cursa.curso=row[0]
            cursa.letra=row[1]
            cursa.idAsignatura=row[2]
            cursa.dniAlumno=row[3]
            lista.append(cursa)
            #print row[0], row[1]
            row = cursor.fetchone()

        cursor.close()
        db.close()

        return lista