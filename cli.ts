import { Stagehand } from "@browserbasehq/stagehand";
import StagehandConfig from "./stagehand.config.js";
import { parsePrompts, PromptStep } from "./promptsParser.js";

async function main() {
  // Retrieve the prompts file path from the command-line arguments
  const args = process.argv.slice(2);
  if (args.length === 0) {
    console.error("Error: Please provide the path to the prompts.json file.");
    process.exit(1);
  }
  const promptsFilePath = args[0];

  const stagehand = new Stagehand({
    ...StagehandConfig,
  });
  await stagehand.init();
  const page = stagehand.page;

  // Parse the provided prompts file
  const prompts = await parsePrompts(promptsFilePath);

  // Execute steps dynamically
  for (const step of prompts) {
    if (step.goto) {
      await page.goto(step.goto);
    }
    if (step.act) {
      await page.act(step.act);
    }
    if (step.wait) {
      await page.waitForTimeout(step.wait * 500); // Convert seconds to milliseconds
    }
  }
}

(async () => {
  await main();
})();