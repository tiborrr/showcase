# Showcase

This is an application that displays various products in a showcase.

## Prerequisites

Before you begin, make sure you have Docker and Docker Compose installed on your machine. For installation instructions refer: 
- [Install Docker](https://docs.docker.com/engine/install/)
- [Install Docker Compose](https://docs.docker.com/compose/install/)

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

1. Clone the repository
    ```sh
    git clone https://github.com/tiborrr/showcase.git
    ```
2. Navigate to the project directory
    ```sh
    cd showcase
    ```
3. Create your `.env` file
    ```sh
    cp .env_sample .env
    ```
   Open the `.env` file and replace the existing values with your actual environment values.

4. Build the Docker images
    ```sh
    docker-compose build
    ```
5. Run the Docker containers
    ```sh
    docker-compose up
    ```

The application should now be up and running at `http://localhost`!

## Authors

- [Tibor](https://github.com/tiborrr)

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details
