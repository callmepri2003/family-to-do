import os
from django.core.management import call_command
from django.http import JsonResponse

def run_command(request):
    # Ensure this endpoint is secured with an environment variable token
    if request.GET.get('token') != os.getenv("COMMAND_RUNNER_TOKEN"):
        return JsonResponse({"error": "Unauthorized"}, status=403)

    command = request.GET.get('command', None)
    if not command:
        return JsonResponse({"error": "No command specified"}, status=400)

    try:
        call_command(command)
        return JsonResponse({"status": f"Command '{command}' executed successfully."})
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=500)
