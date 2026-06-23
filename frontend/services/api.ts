export type Lead = {
  id: number;
  company_name: string;
  website?: string | null;
  email?: string | null;
  industry?: string | null;
  country?: string | null;
  contact_person?: string | null;
  score?: number | null;
  priority: "LOW" | "MEDIUM" | "HIGH";
  status: string;
  created_at: string;
};

const API_BASE = process.env.NEXT_PUBLIC_API_BASE_URL ?? "http://127.0.0.1:8000/api";

export async function getLeads(): Promise<Lead[]> {
  const response = await fetch(`${API_BASE}/leads`, { cache: "no-store" });
  if (!response.ok) {
    throw new Error("Failed to load leads");
  }
  return response.json();
}

export async function createLead(payload: Partial<Lead>) {
  const response = await fetch(`${API_BASE}/leads`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(payload)
  });
  if (!response.ok) {
    throw new Error("Failed to create lead");
  }
  return response.json();
}

export async function runLeadWorkflow(leadId: number) {
  const response = await fetch(`${API_BASE}/leads/${leadId}/run`, { method: "POST" });
  if (!response.ok) {
    throw new Error("Failed to run workflow");
  }
  return response.json();
}

