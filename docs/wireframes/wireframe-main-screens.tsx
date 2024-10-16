import React, { useState } from 'react';
import { Card, CardHeader, CardContent, CardTitle } from "@/components/ui/card"
import { Button } from "@/components/ui/button"
import { Input } from "@/components/ui/input"
import { BarChart, Users, FileText, UserMinus } from 'lucide-react'

const Wireframe = () => {
  const [activeTab, setActiveTab] = useState('dashboard');

  const engineers = [
    { name: '山田太郎', skills: 'Java, Python', project: 'A社システム開発' },
    { name: '鈴木花子', skills: 'JavaScript, React', project: 'B社Webアプリ開発' },
    { name: '佐藤次郎', skills: 'C#, .NET', project: '待機中' },
    { name: '田中美穂', skills: 'PHP, Laravel', project: 'C社ECサイト構築' },
    { name: '高橋健太', skills: 'Python, Django', project: 'D社データ分析システム' },
  ];

  const projects = [
    { name: 'A社システム開発', client: 'A株式会社', status: '進行中', engineers: '山田太郎, 鈴木花子' },
    { name: 'B社Webアプリ開発', client: 'B株式会社', status: '計画中', engineers: '鈴木花子' },
    { name: 'C社ECサイト構築', client: 'C株式会社', status: '進行中', engineers: '田中美穂' },
    { name: 'D社データ分析システム', client: 'D株式会社', status: '完了', engineers: '高橋健太' },
    { name: 'E社モバイルアプリ開発', client: 'E株式会社', status: '提案中', engineers: '未定' },
  ];

  const reports = [
    { date: '2024-10-16', engineer: '山田太郎', project: 'A社システム開発', content: 'データベース設計' },
    { date: '2024-10-16', engineer: '鈴木花子', project: 'B社Webアプリ開発', content: 'フロントエンド実装' },
    { date: '2024-10-16', engineer: '田中美穂', project: 'C社ECサイト構築', content: 'API開発' },
    { date: '2024-10-16', engineer: '高橋健太', project: 'D社データ分析システム', content: 'データクレンジング' },
    { date: '2024-10-16', engineer: '佐藤次郎', project: '研修', content: 'Javaプログラミング演習' },
  ];

  return (
    <div className="p-4">
      <h1 className="text-2xl font-bold mb-4">エンジニア管理システム - ワイヤーフレーム</h1>
      <div className="flex mb-4">
        {['dashboard', 'engineers', 'projects', 'reports'].map((tab) => (
          <Button 
            key={tab} 
            variant={activeTab === tab ? 'default' : 'outline'}
            onClick={() => setActiveTab(tab)}
            className="mr-2"
          >
            {tab === 'dashboard' ? 'ダッシュボード' :
             tab === 'engineers' ? 'エンジニア一覧' :
             tab === 'projects' ? '案件管理' : '日報管理'}
          </Button>
        ))}
      </div>
      
      {activeTab === 'dashboard' && (
        <Card>
          <CardHeader>
            <CardTitle>ダッシュボード</CardTitle>
          </CardHeader>
          <CardContent>
            <div className="grid grid-cols-3 gap-4 mb-4">
              {[
                { title: 'エンジニア総数', icon: Users, value: 150 },
                { title: '待機中エンジニア', icon: UserMinus, value: 30 },
                { title: '未提出日報数', icon: FileText, value: 15 },
              ].map((item, index) => (
                <Card key={index}>
                  <CardHeader>
                    <CardTitle>{item.title}</CardTitle>
                  </CardHeader>
                  <CardContent>
                    <item.icon size={24} />
                    <p className="text-2xl font-bold">{item.value}</p>
                  </CardContent>
                </Card>
              ))}
            </div>
            <Card>
              <CardHeader>
                <CardTitle>エンジニアステータス分布</CardTitle>
              </CardHeader>
              <CardContent>
                <BarChart size={200} />
              </CardContent>
            </Card>
          </CardContent>
        </Card>
      )}
      
      {activeTab === 'engineers' && (
        <Card>
          <CardHeader>
            <CardTitle>エンジニア一覧</CardTitle>
          </CardHeader>
          <CardContent>
            <div className="flex justify-between mb-4">
              <Input placeholder="エンジニアを検索" className="w-1/3" />
              <Button>新規エンジニア追加</Button>
            </div>
            <div className="overflow-x-auto">
              <table className="w-full">
                <thead>
                  <tr className="border-b">
                    <th className="p-2 text-left">名前</th>
                    <th className="p-2 text-left">スキル</th>
                    <th className="p-2 text-left">現在の案件</th>
                    <th className="p-2 text-left">アクション</th>
                  </tr>
                </thead>
                <tbody>
                  {engineers.map((engineer, index) => (
                    <tr key={index} className="border-b">
                      <td className="p-2">{engineer.name}</td>
                      <td className="p-2">{engineer.skills}</td>
                      <td className="p-2">{engineer.project}</td>
                      <td className="p-2">
                        <Button variant="outline" size="sm" className="mr-2">詳細</Button>
                        <Button variant="outline" size="sm">編集</Button>
                      </td>
                    </tr>
                  ))}
                </tbody>
              </table>
            </div>
          </CardContent>
        </Card>
      )}
      
      {activeTab === 'projects' && (
        <Card>
          <CardHeader>
            <CardTitle>案件管理</CardTitle>
          </CardHeader>
          <CardContent>
            <div className="flex justify-between mb-4">
              <Input placeholder="案件を検索" className="w-1/3" />
              <Button>新規案件追加</Button>
            </div>
            <div className="overflow-x-auto">
              <table className="w-full">
                <thead>
                  <tr className="border-b">
                    <th className="p-2 text-left">案件名</th>
                    <th className="p-2 text-left">クライアント</th>
                    <th className="p-2 text-left">ステータス</th>
                    <th className="p-2 text-left">担当エンジニア</th>
                    <th className="p-2 text-left">アクション</th>
                  </tr>
                </thead>
                <tbody>
                  {projects.map((project, index) => (
                    <tr key={index} className="border-b">
                      <td className="p-2">{project.name}</td>
                      <td className="p-2">{project.client}</td>
                      <td className="p-2">{project.status}</td>
                      <td className="p-2">{project.engineers}</td>
                      <td className="p-2">
                        <Button variant="outline" size="sm" className="mr-2">詳細</Button>
                        <Button variant="outline" size="sm">編集</Button>
                      </td>
                    </tr>
                  ))}
                </tbody>
              </table>
            </div>
          </CardContent>
        </Card>
      )}
      
      {activeTab === 'reports' && (
        <Card>
          <CardHeader>
            <CardTitle>日報管理</CardTitle>
          </CardHeader>
          <CardContent>
            <div className="flex justify-between mb-4">
              <Input type="date" className="w-1/3" />
            </div>
            <div className="overflow-x-auto">
              <table className="w-full">
                <thead>
                  <tr className="border-b">
                    <th className="p-2 text-left">日付</th>
                    <th className="p-2 text-left">エンジニア名</th>
                    <th className="p-2 text-left">案件名</th>
                    <th className="p-2 text-left">業務内容</th>
                    <th className="p-2 text-left">アクション</th>
                  </tr>
                </thead>
                <tbody>
                  {reports.map((report, index) => (
                    <tr key={index} className="border-b">
                      <td className="p-2">{report.date}</td>
                      <td className="p-2">{report.engineer}</td>
                      <td className="p-2">{report.project}</td>
                      <td className="p-2">{report.content}</td>
                      <td className="p-2">
                        <Button variant="outline" size="sm" className="mr-2">詳細</Button>
                        <Button variant="outline" size="sm">編集</Button>
                      </td>
                    </tr>
                  ))}
                </tbody>
              </table>
            </div>
          </CardContent>
        </Card>
      )}
    </div>
  );
};

export default Wireframe;
