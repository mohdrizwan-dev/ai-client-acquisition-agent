import { BarChart3, Brain, BriefcaseBusiness, MailCheck } from "lucide-react";
import { LeadForm } from "@/components/lead-form";
import { LeadTable } from "@/components/lead-table";
import { getLeads, type Lead } from "@/services/api";

export default async function DashboardPage() {
  let leads: Lead[] = [];

  try {
    leads = await getLeads();
  } catch {
    leads = [];
  }

  const total = leads.length;
  const highPriority = leads.filter((lead) => lead.priority === "HIGH").length;
  const contacted = leads.filter((lead) => lead.status === "contacted").length;
  const avgScore = total ? Math.round(leads.reduce((sum, lead) => sum + (lead.score ?? 0), 0) / total) : 0;

  return (
    <main className="min-h-screen bg-[#f7f8fb]">
      <header className="border-b border-slate-200 bg-white">
        <div className="mx-auto flex max-w-7xl items-center justify-between px-5 py-5">
          <div>
            <h1 className="text-xl font-semibold text-slate-950">AI Client Acquisition Agent</h1>
            <p className="mt-1 text-sm text-slate-500">Lead discovery, audits, proposals, outreach, and CRM tracking.</p>
          </div>
          <div className="hidden items-center gap-2 rounded-md border border-slate-200 px-3 py-2 text-sm font-medium text-slate-700 md:flex">
            <Brain className="h-4 w-4 text-signal" />
            Human-approved automation
          </div>
        </div>
      </header>

      <section className="mx-auto grid max-w-7xl gap-4 px-5 py-5 md:grid-cols-4">
        <Metric icon={<BriefcaseBusiness className="h-5 w-5" />} label="Total Leads" value={total} />
        <Metric icon={<BarChart3 className="h-5 w-5" />} label="Avg Score" value={avgScore} />
        <Metric icon={<Brain className="h-5 w-5" />} label="High Priority" value={highPriority} />
        <Metric icon={<MailCheck className="h-5 w-5" />} label="Contacted" value={contacted} />
      </section>

      <section className="mx-auto max-w-7xl px-5 pb-8">
        <div className="overflow-hidden rounded-lg border border-slate-200 bg-white">
          <div className="flex items-center justify-between border-b border-slate-200 px-5 py-4">
            <div>
              <h2 className="text-base font-semibold text-slate-950">Lead Command Center</h2>
              <p className="mt-1 text-sm text-slate-500">Add leads manually, then run the MVP agent workflow.</p>
            </div>
          </div>
          <LeadForm />
          <LeadTable leads={leads} />
        </div>
      </section>
    </main>
  );
}

function Metric({ icon, label, value }: { icon: React.ReactNode; label: string; value: number }) {
  return (
    <div className="rounded-lg border border-slate-200 bg-white p-4">
      <div className="flex items-center justify-between">
        <span className="text-sm font-medium text-slate-500">{label}</span>
        <span className="text-signal">{icon}</span>
      </div>
      <div className="mt-3 text-2xl font-semibold text-slate-950">{value}</div>
    </div>
  );
}
