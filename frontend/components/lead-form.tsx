"use client";

import { Plus } from "lucide-react";
import { createLead } from "@/services/api";

export function LeadForm() {
  async function submit(formData: FormData) {
    await createLead({
      company_name: String(formData.get("company_name")),
      website: String(formData.get("website") || ""),
      email: String(formData.get("email") || ""),
      industry: String(formData.get("industry") || ""),
      country: String(formData.get("country") || ""),
      contact_person: String(formData.get("contact_person") || "")
    });
    window.location.reload();
  }

  return (
    <form action={submit} className="grid gap-3 border-b border-slate-200 bg-white p-5 md:grid-cols-6">
      <input className="h-10 rounded-md border border-slate-300 px-3 text-sm md:col-span-2" name="company_name" placeholder="Company name" required />
      <input className="h-10 rounded-md border border-slate-300 px-3 text-sm" name="website" placeholder="Website" />
      <input className="h-10 rounded-md border border-slate-300 px-3 text-sm" name="email" placeholder="Email" />
      <input className="h-10 rounded-md border border-slate-300 px-3 text-sm" name="industry" placeholder="Industry" />
      <input className="h-10 rounded-md border border-slate-300 px-3 text-sm" name="country" placeholder="Country" />
      <input className="h-10 rounded-md border border-slate-300 px-3 text-sm md:col-span-2" name="contact_person" placeholder="Contact person" />
      <button className="inline-flex h-10 items-center justify-center gap-2 rounded-md bg-signal px-4 text-sm font-semibold text-white hover:bg-teal-800" title="Add lead">
        <Plus className="h-4 w-4" />
        Add Lead
      </button>
    </form>
  );
}

