import requests

BASE_URL = "https://jsonplaceholder.typicode.com"

def get_posts():
    response = requests.get(f"{BASE_URL}/posts")
    if response.status_code == 200:
        print("Lista de posts obtenida con éxito:")
        print(response.json())
    else:
        print(f"Error al obtener los posts: {response.status_code}")

def create_post(title, body, user_id):
    data = {"title": title, "body": body, "userId": user_id}
    response = requests.post(f"{BASE_URL}/posts", json=data)
    if response.status_code == 201:
        print("Post creado con éxito:")
        print(response.json())
    else:
        print(f"Error al crear el post: {response.status_code}")

def update_post(post_id, title, body, user_id):
    data = {"title": title, "body": body, "userId": user_id}
    response = requests.put(f"{BASE_URL}/posts/{post_id}", json=data)
    if response.status_code == 200:
        print("Post actualizado con éxito:")
        print(response.json())
    else:
        print(f"Error al actualizar el post: {response.status_code}")

def patch_post(post_id, title):
    data = {"title": title}
    response = requests.patch(f"{BASE_URL}/posts/{post_id}", json=data)
    if response.status_code == 200:
        print("Post actualizado parcialmente con éxito:")
        print(response.json())
    else:
        print(f"Error al actualizar parcialmente el post: {response.status_code}")

def delete_post(post_id):
    response = requests.delete(f"{BASE_URL}/posts/{post_id}")
    if response.status_code == 200:
        print("Post eliminado con éxito.")
    else:
        print(f"Error al eliminar el post: {response.status_code}")

# Ejemplo de uso
if __name__ == "__main__":
    get_posts()
    create_post("Nuevo título", "Este es el cuerpo del post", 1)
    update_post(1, "Título actualizado", "Cuerpo actualizado", 1)
    patch_post(1, "Título parcialmente actualizado")
    delete_post(1)