import { Stagehand, Page, BrowserContext } from "@browserbasehq/stagehand";
import StagehandConfig from "./stagehand.config.js";

async function example() {
  const stagehand = new Stagehand({
    ...StagehandConfig,
  });
  await stagehand.init();
  const page = stagehand.page;
  await page.goto("https://www.youtube.com");
  await page.act(
    "on search bar click and search retro tamil trailer, click on search icon or click enter",
  );

  await page.act("Click the first link");
  await page.act("Click the play button");

  // wait for the video to end
  await page.waitForTimeout(10000);z
}

(async () => {
  await example();
})();
