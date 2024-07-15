
// selecciona BD gpon
db = db.getSiblingDB('gpon');

// crea colección gpon_olt
db.createCollection('gpon_olt');

print('Database and collection created.');