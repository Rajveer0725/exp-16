import { describe, it, expect } from "vitest";

function add(a, b) {
  return a + b;
}

describe("Addition Test", () => {
  it("adds numbers correctly", () => {
    expect(add(2, 3)).toBe(5);
  });
});