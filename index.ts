import { Stagehand } from "@browserbasehq/stagehand";
type AutomationPrompt = {
  action: string; // e.g., "Click", "Fill", "Submit"
  selector?: string; // CSS selector for the element to act on
  value?: string; // Value to fill in case of input actions
};

async function executeAutomation(prompts: AutomationPrompt[]) {
  const page = await Stagehand.open();

  for (const prompt of prompts) {
    switch (prompt.action) {
      case "Click":
        if (!prompt.selector) throw new Error("Missing selector for 'Click' action");
        await page.click(prompt.selector);
        break;

      case "Fill":
        if (!prompt.selector || !prompt.value) throw new Error("Missing selector or value for 'Fill' action");
        await page.fill(prompt.selector, prompt.value);
        break;

      case "Submit":
        if (!prompt.selector) throw new Error("Missing selector for 'Submit' action");
        await page.click(prompt.selector);
        break;

      default:
        console.warn(`Unknown action: ${prompt.action}`);
    }
  }

  console.log("Automation complete!");
}

export default executeAutomation;