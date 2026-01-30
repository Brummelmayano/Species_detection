import httpx
from typing import List, Dict, Any
from ..config import settings

class SpeciesNetService:
    def __init__(self):
        self.base_url = settings.speciesnet_url

    async def detect_species(self, image_url: str) -> List[Dict[str, Any]]:
        """
        Envoie une image à SpeciesNet pour détection d'espèces
        """
        async with httpx.AsyncClient() as client:
            try:
                response = await client.post(
                    f"{self.base_url}/detect",
                    json={"image_url": image_url},
                    timeout=60.0  # Timeout de 60 secondes
                )
                response.raise_for_status()
                result = response.json()

                # Normaliser le format de réponse
                detections = []
                for detection in result.get("detections", []):
                    detections.append({
                        "species_name": detection.get("species", "unknown"),
                        "confidence_score": detection.get("confidence", 0.0),
                        "bbox_x_min": detection.get("bbox", {}).get("x_min", 0),
                        "bbox_y_min": detection.get("bbox", {}).get("y_min", 0),
                        "bbox_x_max": detection.get("bbox", {}).get("x_max", 0),
                        "bbox_y_max": detection.get("bbox", {}).get("y_max", 0),
                        "bbox_width": detection.get("bbox", {}).get("width"),
                        "bbox_height": detection.get("bbox", {}).get("height")
                    })

                return detections

            except httpx.RequestError as exc:
                print(f"Erreur de requête SpeciesNet: {exc}")
                raise Exception(f"Erreur de communication avec SpeciesNet: {exc}")
            except httpx.HTTPStatusError as exc:
                print(f"Erreur HTTP SpeciesNet: {exc.response.status_code}")
                raise Exception(f"Erreur du service SpeciesNet: {exc.response.status_code}")

    async def get_model_info(self) -> Dict[str, Any]:
        """
        Récupère les informations sur le modèle SpeciesNet
        """
        async with httpx.AsyncClient() as client:
            try:
                response = await client.get(f"{self.base_url}/info")
                response.raise_for_status()
                return response.json()
            except Exception as exc:
                print(f"Erreur récupération info modèle: {exc}")
                return {"status": "unavailable"}