
from django.http import HttpResponse

def index(request):
    host = request.META["HTTP_HOST"]
    user_agent = request.META["HTTP_USER_AGENT"]
    path = request.path
    ip = request.META["REMOTE_ADDR"]

    return HttpResponse (f"""
        <p>Host:{host}</p>
        <p>Path: {path}</p>
        <p>User-agent: {user_agent} </p>
        <p>ip: {ip} <p>
        """)

def error(request):
    return HttpResponse("Произошла кибератака", status=400, reason="cyberattack")


def user(request, name="Underfined", name_folder="Underfined", num_post=0):
    return HttpResponse(f"""
        <p>Name: {name} </p>
        <p>Name-Folder: {name_folder} </p>
        <p>Post-Number: {num_post} </p>
    """)