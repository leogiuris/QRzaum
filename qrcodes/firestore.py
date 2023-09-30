import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

cred = credentials.Certificate("firebase.json")
firebase_admin.initialize_app(cred)
db = firestore.client()


def create(collection, data):
    """
        create() : Add document to Firestore collection with request body.
        Ensure you pass a custom ID as part of json body in post request,
        e.g. json={'id': '1', 'title': 'Write a blog post'}
    """

    collection_ref = db.collection(collection)

    try:
        id = data['id']
        collection_ref.document(id).set(data)
        return {"success": True}, 200
    except Exception as e:
        return f"An Error Occurred: {e}"


def createMany(collection, data):
    batch = db.batch()
    collection_ref = db.collection(collection)
    try:
        for item in data:
            doc_ref = collection_ref.document(item["id"])
            batch.set(doc_ref, item)

        batch.commit()

        return {"success": True}, 200
    except Exception as e:
        return f"An Error Occurred: {e}"


def read(collection, id=None):
    """
        read() : Fetches documents from Firestore collection as JSON.
        doc : Return document that matches query ID.
        all_doc : Return all documents.
    """
    collection_ref = db.collection(collection)

    try:
        # Check if ID was passed to URL query
        doc_id = id
        if doc_id:
            doc = collection_ref.document(doc_id).get()
            return doc.to_dict(), 200
        else:
            all_doc = [doc.to_dict() for doc in collection_ref.stream()]
            return all_doc, 200
    except Exception as e:
        return f"An Error Occurred: {e}"


def update(collection, data):
    """
        update() : Update document in Firestore collection with request body.
        Ensure you pass a custom ID as part of json body in post request,
        e.g. json={'id': '1', 'title': 'Write a blog post today'}
    """
    collection_ref = db.collection(collection)

    try:
        id = data['id']
        collection_ref.document(id).update(data)
        return {"success": True}, 200
    except Exception as e:
        return f"An Error Occurred: {e}"


def updateMany(collection, data):
    """
        batch = db.batch()

        # Set the data for NYC
        nyc_ref = db.collection("cities").document("NYC")
        batch.set(nyc_ref, {"name": "New York City"})

        # Update the population for SF
        sf_ref = db.collection("cities").document("SF")
        batch.update(sf_ref, {"population": 1000000})

        # Delete DEN
        den_ref = db.collection("cities").document("DEN")
        batch.delete(den_ref)

        # Commit the batch
        batch.commit()
    """
    batch = db.batch()
    collection_ref = db.collection(collection)

    try:
        for item in data:
            doc_ref = collection_ref.document(item["id"])
            batch.update(doc_ref, item)

        batch.commit()

        return {"success": True}, 200
    except Exception as e:
        return f"An Error Occurred: {e}"


def delete(collection, id):
    """
        delete() : Delete a document from Firestore collection.
    """
    collection_ref = db.collection(collection)

    try:
        # Check for ID in URL query
        collection_ref.document(id).delete()
        return {"success": True}, 200
    except Exception as e:
        return f"An Error Occurred: {e}"
