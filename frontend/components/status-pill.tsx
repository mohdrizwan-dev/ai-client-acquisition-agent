import { CheckCircle2, CircleDashed, Flame, Send } from "lucide-react";

type StatusPillProps = {
  value: string;
};

const styles: Record<string, string> = {
  HIGH: "bg-red-50 text-red-700 ring-red-200",
  MEDIUM: "bg-amber-50 text-amber-700 ring-amber-200",
  LOW: "bg-slate-100 text-slate-700 ring-slate-200",
  contacted: "bg-teal-50 text-teal-700 ring-teal-200",
  analyzed: "bg-blue-50 text-blue-700 ring-blue-200",
  closed: "bg-emerald-50 text-emerald-700 ring-emerald-200"
};

export function StatusPill({ value }: StatusPillProps) {
  const Icon = value === "HIGH" ? Flame : value === "contacted" ? Send : value === "closed" ? CheckCircle2 : CircleDashed;

  return (
    <span className={`inline-flex h-7 items-center gap-1.5 rounded-md px-2.5 text-xs font-medium ring-1 ${styles[value] ?? "bg-white text-slate-700 ring-slate-200"}`}>
      <Icon className="h-3.5 w-3.5" />
      {value}
    </span>
  );
}

