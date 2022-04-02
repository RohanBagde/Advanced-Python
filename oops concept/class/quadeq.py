{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "#quadeq.py-->this name treated as module name we are use this module for next program\n",
    "\n",
    "class quad:\n",
    "    def readvalues(self):  ##create def fun for input for read value\n",
    "        self.a=float(input(\"enter the value of A: \"))\n",
    "        self.b=float(input(\"enter the value of B: \"))\n",
    "        self.c=float(input(\"enter the value of C: \"))\n",
    "    def calroot(self):     #create def fun for calculate  value\n",
    "        self.r1=(-self.b+(self.b**2-4*self.a*self.c)**0.5)/(2*self.a)\n",
    "        self.r2=(-self.b-(self.b**2-4*self.a*self.c)**0.5)/(2*self.a)\n",
    "    def dispresult(self):  #create def fnc for print values\n",
    "        print(\"value of a={}\".format(self.a))\n",
    "        print(\"value of b={}\".format(self.b))\n",
    "        print(\"value of c={}\".format(self.c))\n",
    "        print(\"root 1={}\".format(self.r1))\n",
    "        print(\"root 2={}\".format(self.r2))"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
