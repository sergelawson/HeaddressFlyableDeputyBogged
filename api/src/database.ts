import { DataSource } from "typeorm";

const myDataSource = new DataSource({
  type: "postgres",
  host: "postgres",
  port: 5432,
  username: "postgres",
  password: "testtest",
  database: "postgres",
  logging: true,
  synchronize: true,
});

export default myDataSource;
