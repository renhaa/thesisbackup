%
% input:
% - U3  : matrix of expressions: [ num_expression x dim ]
% - L3  : scalar value to define the dimension of apathy vertex with:  L3 <= dim
% - ExL : vector of length 2, giving the the number of emotions and the
%         corresponding levels
%
function[apathy_vertex]= get_apathy_vertex(U3,L3,ExL)
bool_plot = false;

if nargin<3
    E          = 6; % num emotions
    num_levels = 4; % num level
else
    E = ExL(1);
    num_levels = ExL(2);
end
if nargin<2
    L3 = 3;
end
if size(U3,1)==num_levels*E+1 % omit neutral for estimation
    U3 = U3(2:end,:);
elseif size(U3,1)~=E*num_levels
    error('unexpected input size size(U3)=[%i,%i] do not match params [%i,%i]',size(U3,1),size(U3,2),E,num_levels)
end
U3 = U3(:,1:L3);

indices = reshape(1:E*num_levels,num_levels,[])';
M = zeros(L3,E);
N = M;
if bool_plot
    ms = 15;
    lw = 2;
    figure(1), clf,
end

for iemotion=1:E
    U3_e = U3(indices(iemotion,:),:);
    
    P = U3_e; % pick one row of U3
    mu_e = mean(P,1);
    P = P-repmat(mu_e,num_levels,1);
    [coeff,score,latent] = pca(P);
    
    v = coeff(:,1)';
    v = v./norm(v);
    M(:,iemotion)=mu_e;
    N(:,iemotion)=v;
    if bool_plot
        
        subplot(2,3,iemotion)
        plot3(U3(:,1),U3(:,2),U3(:,3),'k.','markersize',15)
        hold on
        plot3(U3_e(:,1),U3_e(:,2),U3_e(:,3),'bx','markersize',ms,'linewidth',lw)
        axis equal
        plot3(mu_e(:,1),mu_e(:,2),mu_e(:,3),'r+','markersize',ms,'linewidth',lw)
        p = [mu_e; mu_e+v];
        plot3(p(:,1),p(:,2),p(:,3),'c-','linewidth',1.5)
        % mu_e = zeros(1,3);
        % p = [mu_e; mu_e+v];
        % plot3(p(:,1),p(:,2),p(:,3),'c-','linewidth',1.5)
        axis equal
        grid on
    end
end
xinit = ones(E,1)./E;
% xinit = rand(E,1);
f       = @(x) get_dist_to_lines_p(M,N,x);
options = optimoptions('fminunc','Algorithm','trust-region','SpecifyObjectiveGradient',true,'display','off');
x       = fminunc(f,xinit,options);

alpha = x;
p = 0;
for i=1:E
    p = p + M(:,i)+N(:,i)*alpha(i);
end
p = p./E;
apathy_vertex = p(:)';

end