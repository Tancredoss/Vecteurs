from math import sqrt

class Vect3D():
    def __init__(self,dx=0,dy=0,dz=0):
        self.dx = dx
        self.dy = dy
        self.dz = dz
    def __add__(self, other):
        return Vect3D(self.dx+other.dx,self.dy + other.dy,self.dz + other.dz)
    def __radd__(self, other):
        return Vect3D(self.dx+other.dx,self.dy + other.dy,self.dz + other.dz)
    def __repr__(self):
        return 'Vect({},{},{})'.format(self.dx,self.dy,self.dz)
    def __sub__(self,other):
        return Vect3D(self.dx - other.dx,self.dy - other.dy,self.dz - other.dz)
    def __rsub__(self,other):
        return Vect3D(self.dx - other.dx,self.dy - other.dy,self.dz - other.dz)
    def __str__(self):
        return '({},{},{})'.format(self.dx,self.dy,self.dz)
    def __xor__(self,other):
        return Vect3D(self.dy*other.dz-self.dz*other.dy,self.dz*other.dx-self.dx*other.dz,self.dx*other.dy-self.dy*other.dx)
    def __neg__(self):
        return Vect3D(-self.dx,-self.dy,-self.dz)
    def __getitem__(self, coord):
        if coord == "x" or coord == 0:
            return self.dx
        elif coord == "y" or coord == 1:
            return self.dy
        elif coord == "z" or coord == 2:
            return self.dz
        raise NameError("Invalid Coordinate")
    def __setitem__(self,coord,value):
        if type(value) != int:
            raise "Invalid Value"
        if coord == "x" or coord == 0:
            self.dx = value
        elif coord == "y" or coord == 1:
            self.dy = value
        elif coord == "z" or coord == 2:
            self.dz = value
        else:
            raise NameError("Invalid Coordinate")
    def __mul__(self,scal):
        return Vect3D(self.dx * scal, self.dy * scal, self.dz * scal)
    def __rmul__(self,scal):
        return Vect3D(self.dx * scal, self.dy * scal, self.dz * scal)
    def __eq__(self,other):
        return (self.dx == other.dx) and (self.dy == other.dy) and (self.dz == other.dz)
    def __ne__(self,other):
        return not((self.dx == other.dx) and (self.dy == other.dy) and (self.dz == other.dz))
    def __iadd__(self,other):
        self.dx += other.dx
        self.dy += other.dy
        self.dz += other.dz
        return self
    def __isub__(self,other):
        self.dx -= other.dx
        self.dy -= other.dy
        self.dz -= other.dz
        return self
    def __imul__(self,scal):
        self.dx *= scal
        self.dy *= scal
        self.dz *= scal
        return self
    def __matmul__(self,other):
        return dot(self,other)
    def norme(self):
        return sqrt(self.dx**2 + self.dy**2 + self.dz**2)

class Vect2D():
    def __init__(self,dx=0,dy=0):
        self.dx = dx
        self.dy = dy
    def __add__(self, other):
        return Vect2D(self.dx+other.dx,self.dy + other.dy)
    def __radd__(self, other):
        return Vect2D(self.dx+other.dx,self.dy + other.dy)
    def __repr__(self):
        return 'Vect({},{})'.format(self.dx,self.dy)
    def __sub__(self,other):
        return Vect2D(self.dx - other.dx,self.dy - other.dy)
    def __rsub__(self,other):
        return Vect2D(self.dx - other.dx,self.dy - other.dy)
    def __str__(self):
        return '({},{})'.format(self.dx,self.dy)
    def __neg__(self):
        return Vect2D(-self.dx,-self.dy)
    def __getitem__(self, coord):
        if coord == "x" or coord == 0:
            return self.dx
        elif coord == "y" or coord == 1:
            return self.dy
        raise NameError("Invalid Coordinate")
    def __setitem__(self,coord,value):
        if type(value) != int:
            raise "Invalid Value"
        if coord == "x" or coord == 0:
            self.dx = value
        elif coord == "y" or coord == 1:
            self.dy = value
        else:
            raise NameError("Invalid Coordinate")
    def __mul__(self,scal):
        return Vect2D(self.dx * scal, self.dy * scal)
    def __rmul__(self,scal):
        return Vect2D(self.dx * scal, self.dy * scal)
    def __eq__(self,other):
        return (self.dx == other.dx) and (self.dy == other.dy)
    def __ne__(self,other):
        return not((self.dx == other.dx) and (self.dy == other.dy))
    def __iadd__(self,other):
        self.dx += other.dx
        self.dy += other.dy
        return self
    def __isub__(self,other):
        self.dx -= other.dx
        self.dy -= other.dy
        return self
    def __imul__(self,scal):
        self.dx *= scal
        self.dy *= scal
        return self
    def __matmul__(self,other):
        return dot(self,other)
    def norme(self):
        return sqrt(self.dx**2 + self.dy**2)

def norme(vecteur):
    """Renvoie la norme d'un object de type Vect"""
    return vecteur.norme()
def dot(vect1,vect2):
    """Renvoie le produit scalaire de deux vecteurs"""
    try :
        return vect1.dx*vect2.dx + vect1.dy*vect2.dy + vect1.dz*vect2.dz
    except :
        return vect1.dx*vect2.dx + vect1.dy*vect2.dy
        

def null3D():
    """Renvoie le vecteur nul à 3 dimensions"""
    return Vect3D(0,0,0)

def null2D():
    """Renvoie le vecteur nul à deux dimensions"""
    return Vect2D(0,0)


if __name__ == "__main__":
    A = Vect3D(2,3,6)
    B = Vect3D(5,1,-2)
    print(A)
    C = A^B
    print(C)
    D = Vect2D(1,4)
    E = Vect2D(6,3)
    print(E)
    F = D-E
    print(F)
