import { NextResponse } from "next/server";

export async function POST(req: Request) {
  try {
    const { email } = await req.json();
    if (typeof email !== "string" || !/[^@\s]+@[^@\s]+\.[^@\s]+/.test(email)) {
      return NextResponse.json({ ok: false, error: "invalid_email" }, { status: 400 });
    }

    // TODO: Integrate with your email provider (Klaviyo, Mailchimp, ConvertKit, etc.)
    // This is a placeholder success response.

    return NextResponse.json({ ok: true });
  } catch {
    return NextResponse.json({ ok: false, error: "bad_request" }, { status: 400 });
  }
}
