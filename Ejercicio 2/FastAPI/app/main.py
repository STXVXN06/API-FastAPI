from fastapi import FastAPI
from starlette.responses import RedirectResponse

# Routes
from routes.user_route import user_router
from routes.order_route import order_router
from routes.pet_route import pet_router
from routes.product_route import product_router
from routes.vehicle_route import vehicle_router

from contextlib import asynccontextmanager
from database import database as connection


@asynccontextmanager
async def lifespan(app: FastAPI):
    #Conectar a la base de datos si la conexion esta cerrada
    if connection.is_closed():
        connection.connect()
    
    try:
        yield # Aqui se ejecuta la aplicacion
    finally:
        if not connection.is_closed():
            connection.close()

app = FastAPI(lifespan=lifespan)

# On Startup
# On Shutdown

# Documentacion
@app.get("/")
async def docs():
    return RedirectResponse(url="docs")


# localhost:9090/
# Rutas
app.include_router(user_router, prefix="/users", tags=["Users"])
app.include_router(order_router, prefix="/orders", tags=["Orders"])
app.include_router(pet_router, prefix="/pets", tags=["Pets"])
app.include_router(product_router, prefix="/products", tags=["Products"])
app.include_router(vehicle_router, prefix="/vehicles", tags=["Vechicles"])