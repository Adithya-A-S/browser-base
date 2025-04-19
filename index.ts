import { Stagehand } from "@browserbasehq/stagehand";
import StagehandConfig from "./stagehand.config.js";
import { parsePrompts, PromptStep } from "./promptsParser.js";
import { actWithCache } from "./utils.js"; // Use the cached action handler

async function example() {
  const stagehand = new Stagehand({
    ...StagehandConfig,
  });
  await stagehand.init();
  const page = stagehand.page;

  // Parse prompts.json
  const prompts = await parsePrompts("prompts.json");

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
  await example();
})();