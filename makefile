# Define the default target
run: build
    node ./dist/cli.js ./jio.json

# Build command to compile TypeScript
build:
    npm run build