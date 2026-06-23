"use client";

import { Bot, ExternalLink, Play } from "lucide-react";
import { Lead, runLeadWorkflow } from "@/services/api";
import { StatusPill } from "@/components/status-pill";

type LeadTableProps = {
  leads: Lead[];
};

export function LeadTable({ leads }: LeadTableProps) {
  async function runWorkflow(id: number) {
    await runLeadWorkflow(id);
    window.location.reload();
  }

  return (
    <div className="overflow-hidden border-y border-slate-200 bg-white">
      <table className="w-full min-w-[880px] border-collapse text-left text-sm">
        <thead className="bg-slate-50 text-xs uppercase text-slate-500">
          <tr>
            <th className="px-5 py-3 font-semibold">Company</th>
            <th className="px-5 py-3 font-semibold">Industry</th>
            <th className="px-5 py-3 font-semibold">Priority</th>
            <th className="px-5 py-3 font-semibold">Score</th>
            <th className="px-5 py-3 font-semibold">Status</th>
            <th className="px-5 py-3 font-semibold">Action</th>
          </tr>
        </thead>
        <tbody className="divide-y divide-slate-100">
          {leads.map((lead) => (
            <tr key={lead.id} className="hover:bg-slate-50">
              <td className="px-5 py-4">
                <div className="font-medium text-slate-950">{lead.company_name}</div>
                {lead.website ? (
                  <a className="mt-1 inline-flex items-center gap-1 text-xs text-signal" href={lead.website} target="_blank">
                    {lead.website}
                    <ExternalLink className="h-3 w-3" />
                  </a>
                ) : null}
              </td>
              <td className="px-5 py-4 text-slate-600">{lead.industry ?? "Unclassified"}</td>
              <td className="px-5 py-4"><StatusPill value={lead.priority} /></td>
              <td className="px-5 py-4 font-semibold text-slate-900">{lead.score ?? "-"}</td>
              <td className="px-5 py-4"><StatusPill value={lead.status} /></td>
              <td className="px-5 py-4">
                <button
                  className="inline-flex h-9 items-center gap-2 rounded-md bg-ink px-3 text-xs font-semibold text-white hover:bg-slate-700"
                  onClick={() => runWorkflow(lead.id)}
                  title="Analyze, score, and generate proposal"
                >
                  {lead.status === "new" ? <Play className="h-4 w-4" /> : <Bot className="h-4 w-4" />}
                  Run
                </button>
              </td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}

