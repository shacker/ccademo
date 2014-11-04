import ldap
from random import choice
from string import ascii_lowercase, digits
from django.contrib.auth.models import User
from django.conf import settings

def generate_random_username(length=12, chars=ascii_lowercase+digits, split=4, delimiter=''):

    username = ''.join([choice(chars) for i in xrange(length)])

    if split:
        username = delimiter.join([username[start:start+split] for start in range(0, len(username), split)])

    try:
        User.objects.get(username=username)
        return generate_random_username(length=length, chars=chars, split=split, delimiter=delimiter)
    except User.DoesNotExist:
        return username;



def ldap_connect():
    '''
    Returns an LDAP connection object, to be used by various search functions.
    '''

    # model bash command
    # ldapsearch -x
    #   -b "ou=People,dc=cca,dc=edu"
    #   -D "uid=uadmin,ou=Administrators,ou=TopologyManagement,o=NetscapeRoot"
    #   -W -h directory.cca.edu uid=shacker

    try:
        conn = ldap.initialize(settings.LDAP_SERVER)
        conn.simple_bind_s(settings.LDAP_AUTH_DN, settings.LDAP_PASS)

        print("\nConnected to LDAP server {server}\n".format(server=settings.LDAP_SERVER))

        return conn

    except ldap.SERVER_DOWN:
        print("Connection to LDAP server failed")
        return None


def ldap_get_by_username(username):
        '''
        Given a username, returns all base LDAP data.
        '''

        conn = ldap_connect()
        filter = "(uid={user})".format(user=username)
        results = conn.search_s(settings.LDAP_BASE_DN, ldap.SCOPE_SUBTREE, filter)

        # `results` is a python list containing a single tuple.
        # First element of tuple is the user dn, 2nd is all the data,
        # which can be accessed via e.g.:
        # data['displayName'], data['ccaStudentNumber'], data['loginShell']

        try:
            data = results[0][1]
            return data
        except:
            return False


def ldap_get_by_id(id):
        '''
        Given a student ID or staff ID, returns all base LDAP data.
        TODO: Ambiguous whether to search
        ccaStudentNumber, ccaEmployeeNumber, or employeeNumber field.
        '''

        conn = ldap_connect()
        filter = "(ccaStudentNumber={id})".format(id=id)
        results = conn.search_s(settings.LDAP_BASE_DN, ldap.SCOPE_SUBTREE, filter)

        try:
            data = results[0][1]
            return data
        except:
            return False
