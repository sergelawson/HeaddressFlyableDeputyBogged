import * as express from "express";
import { Request, Response } from "express";
import database from "./database";

// Initializing database
database
  .initialize()
  .then(() => {
    console.log("Database has been initialized!");
  })
  .catch((err) => {
    console.error("Error during database initialization:", err);
  });

const queryManager = database.manager;

const app = express();

app.use(express.json());

app.get("/delineated-fields", async (req: Request, res: Response) => {
  let loglat = req.query.location as string;

  if (!loglat) return res.status(400).json({ message: "please send location" });

  const [log, lat] = loglat.split(",");

  try {
    const result = await queryManager.query(
      "SELECT ST_AsGeoJSON(geometry) FROM fields WHERE ST_Contains(geometry, ST_SetSRID(ST_MakePoint($1, $2), 4326))",
      [log, lat]
    );

    return res.json(result);
  } catch (error) {
    return res.status(500).send("Server error");
  }
});

app.listen(8080);

// http://localhost:8080/delineated-fields?location=11.190343929175015,60.742178240839934
