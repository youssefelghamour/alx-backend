# 0x03. Queuing System in JS

## Overview
This project involves creating a queuing system using Redis and Kue with Node.js and Express.js. It covers the setup of Redis, basic and advanced Redis operations, message publishing and subscribing, and job creation and processing using Kue.

## Files

| File                | Description                                                                                           |
|---------------------|-------------------------------------------------------------------------------------------------------|
| `README.md`         | This file                                                                                           |
| `package.json`      | Project dependencies and configuration                                                                |
| `.babelrc`          | Babel configuration file                                                                             |
| `0-redis_client.js` | Connects to the Redis server and logs connection status                                               |
| `1-redis_op.js`     | Performs basic Redis operations including setting and retrieving values                               |
| `2-redis_op_async.js` | Performs Redis operations using async/await with `promisify`                                          |
| `4-redis_advanced_op.js` | Stores and displays hash values in Redis                                                            |
| `5-subscriber.js`   | Subscribes to a Redis channel and logs received messages                                               |
| `5-publisher.js`    | Publishes messages to a Redis channel with delayed timing                                             |
| `6-job_creator.js`  | Creates a job with Kue and logs job creation and completion                                           |
| `6-job_processor.js`| Processes jobs with Kue and logs notifications                                                         |
| `7-job_creator.js` | Creates an array of jobs and a queue with Kue, then process and track job progress and errors.        |
| `7-job_processor.js` | Create a job processor to handle blacklisted phone numbers, track job progress, and log information. |
| `8-job.js`         | Function to manage job creation and log job status (e.g., creation, completion, failure).   |
| `8-job.test.js`    | Tests for the `createPushNotificationsJobs` function, including job creation and error handling.     |
| `9-stock.js`       | Server with routes to manage product stock and reservation using Redis.                  |
| `100-seat.js`      | An express server to manage seat reservations, track availability, and process reservations.   |
| `dump.rdb`          | Redis database dump file for initializing the Redis server                                            |
