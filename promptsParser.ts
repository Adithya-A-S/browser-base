import fs from "fs/promises";

export interface PromptStep {
  goto?: string;
  act?: string;
  wait?: number;
}

/**
 * Parses the prompts.json file and returns the steps.
 * @param filePath - Path to the prompts.json file.
 * @returns Array of parsed steps.
 */
export async function parsePrompts(filePath: string): Promise<PromptStep[]> {
  try {
    const fileContent = await fs.readFile(filePath, "utf-8");
    const parsedData = JSON.parse(fileContent);
    console.log("Parsed prompts.json:", parsedData); // Debugging line to check the parsed data
    return parsedData.steps || [];
  } catch (error) {
    console.error("Error reading or parsing prompts.json:", error);
    return [];
  }
}