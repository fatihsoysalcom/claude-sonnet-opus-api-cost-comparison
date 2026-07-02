import math

# --- Claude API Pricing (per 1 Million tokens) ---
# Prices are illustrative and based on Anthropic's official pricing as of June 2024.
# Always check the latest pricing on the official website.
CLAUDE_3_OPUS_PRICING = {
    "input_cost_per_million_tokens": 15.00,  # $15.00 / M token
    "output_cost_per_million_tokens": 75.00, # $75.00 / M token
}

CLAUDE_3_5_SONNET_PRICING = {
    "input_cost_per_million_tokens": 3.00,   # $3.00 / M token
    "output_cost_per_million_tokens": 15.00,  # $15.00 / M token
}

def calculate_api_cost(model_pricing, input_tokens, output_tokens):
    """
    Calculates the estimated API cost for a given number of input and output tokens.
    """
    input_cost = (input_tokens / 1_000_000) * model_pricing["input_cost_per_million_tokens"]
    output_cost = (output_tokens / 1_000_000) * model_pricing["output_cost_per_million_tokens"]
    return input_cost + output_cost

def main():
    print("--- Claude API Cost Comparison: Opus vs. Sonnet ---")
    print("Prices are illustrative and based on Anthropic's official pricing as of June 2024.")
    print("Always check the latest pricing on the official website.\n")

    # Define a few hypothetical API call scenarios
    scenarios = [
        {"name": "Short Query, Short Response", "input": 500, "output": 100},
        {"name": "Medium Query, Medium Response", "input": 2000, "output": 500},
        {"name": "Long Query, Detailed Response", "input": 10000, "output": 2000},
        {"name": "Very Long Context, Moderate Response", "input": 50000, "output": 1000},
    ]

    for i, scenario in enumerate(scenarios):
        input_tokens = scenario["input"]
        output_tokens = scenario["output"]
        scenario_name = scenario["name"]

        print(f"Scenario {i+1}: {scenario_name}")
        print(f"  Input Tokens: {input_tokens}, Output Tokens: {output_tokens}")

        # Calculate cost for Claude 3 Opus
        opus_cost = calculate_api_cost(CLAUDE_3_OPUS_PRICING, input_tokens, output_tokens)
        print(f"  Claude 3 Opus Cost: ${opus_cost:.4f}")

        # Calculate cost for Claude 3.5 Sonnet
        sonnet_cost = calculate_api_cost(CLAUDE_3_5_SONNET_PRICING, input_tokens, output_tokens)
        print(f"  Claude 3.5 Sonnet Cost: ${sonnet_cost:.4f}")

        # Calculate savings
        if opus_cost > 0:
            savings = opus_cost - sonnet_cost
            percentage_savings = (savings / opus_cost) * 100
            # This demonstrates the significant cost reduction Sonnet offers over Opus.
            print(f"  Savings with Sonnet: ${savings:.4f} ({percentage_savings:.2f}% cheaper)\n")
        else:
            print("  No cost for Opus, no savings to calculate.\n")

    # Article also mentions 'prompt caching' as a cost optimization technique.
    # While not directly demonstrated here, prompt caching would further reduce input token costs
    # by reusing previous prompts or parts of them, avoiding re-sending identical data to the API.
    print("Note: Prompt caching is another advanced technique to further reduce API costs by reusing")
    print("previously processed prompts, effectively reducing input token usage for repetitive queries.")

if __name__ == "__main__":
    main()
