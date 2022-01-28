from django.shortcuts import render
from rest_framework.views import APIView, Response, status
from .tasks import getAllUsers
# from celery.result import AsyncResult
from ModelSite.celery import app


class GetUsersCeleryView(APIView):
    def get(self, request):
        res = getAllUsers.delay()
        # users_json = json.dumps(users)
        print(res)
        print("Here!")
        info = 'Getting all users, check task %s' % str(res.id)
        message = {'info': info}
        return Response(message, status.HTTP_200_OK)

class CheckTask(APIView):
    def get(self, request, id):
        res = app.AsyncResult(id)
        if res.successful():
            message = res.get()
            return Response(message, status.HTTP_200_OK)
        elif res.failed():
            resStatus = res.state
            message = {"status": resStatus}
            return Response(message, status.HTTP_200_OK)
        else:
            message = {"status": "Waiting for your task!"}
            return Response(message, status.HTTP_200_OK)